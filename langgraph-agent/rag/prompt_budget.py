"""Whole-chunk Frontend RAG packing with output and safety reservations.

Setup: pip install -r requirements-rag.txt
       python -m rag.prompt_budget --prepare-tokenizer
The pinned official Qwen tokenizer and two-message ChatML template match the
local qwen2.5-coder:14b Ollama prompt (validated against prompt_eval_count).
Runtime never downloads assets. Missing assets/other models use a conservative
UTF-8 byte upper bound and retain the existing core prompt unchanged.
"""

import argparse
from functools import lru_cache
import hashlib
from pathlib import Path
import urllib.request

from rag.db_retriever import PROJECT_ROOT, format_db_context
from rag.frontend_retriever import format_frontend_context

TOKENIZER_PATH = PROJECT_ROOT / "rag/tokenizers/qwen2.5-coder-14b.json"
TOKENIZER_SHA256 = "c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539"
TOKENIZER_URL = "https://huggingface.co/Qwen/Qwen2.5-Coder-14B-Instruct/resolve/main/tokenizer.json"
SAFETY_TOKENS = 256


def chatml(system, user):
    return (f"<|im_start|>system\n{system}<|im_end|>\n"
            f"<|im_start|>user\n{user}<|im_end|>\n<|im_start|>assistant\n")


@lru_cache(maxsize=1)
def _load_tokenizer(stamp):
    from tokenizers import Tokenizer
    path = Path(stamp[0])
    with path.open("rb") as stream:
        digest = hashlib.file_digest(stream, "sha256").hexdigest()
    if digest != TOKENIZER_SHA256:
        raise ValueError("Unexpected Qwen tokenizer checksum")
    return Tokenizer.from_file(str(path))


def prompt_counter(model):
    if model == "qwen2.5-coder:14b":
        try:
            stat = TOKENIZER_PATH.stat()
            tokenizer = _load_tokenizer((str(TOKENIZER_PATH), stat.st_mtime_ns, stat.st_size))
            return (lambda system, user: len(tokenizer.encode(
                chatml(system, user), add_special_tokens=False).ids)), "qwen2_chatml"
        except (ImportError, OSError, ValueError):
            pass
    return (lambda system, user: len(chatml(system, user).encode("utf-8"))), "utf8_upper_bound"


def rag_section(results):
    return ("\n\n[Frontend Domain RAG — general technical guidance]\n"
            + format_frontend_context(results)
            + "\n기술 참고용입니다. 예시의 API·기능을 새 요구사항으로 해석하지 마세요. "
              "사용자 요청과 현재 Backend API 계약을 우선하세요.\n[End Frontend Domain RAG]")


def pack_frontend_rag(system, user, results, *, model, num_ctx, num_predict,
                      status="ok", counter=None, rag_headroom=0):
    count, kind = prompt_counter(model) if counter is None else (counter, "test_counter")
    base_tokens = count(system, user)
    limit = num_ctx - num_predict - SAFETY_TOKENS
    rag_limit = limit - max(0, rag_headroom)
    selected = []
    prompt, tokens = user, base_tokens
    for result in results[:3]:
        candidate = user + rag_section([*selected, result])
        candidate_tokens = count(system, candidate)
        if candidate_tokens <= rag_limit:
            selected.append(result)
            prompt, tokens = candidate, candidate_tokens
    if not selected and status in ("search_failed", "empty"):
        notice = ("\n\n[Frontend Domain RAG]\n"
                  "검색된 Domain RAG를 사용할 수 없습니다. 기존 Project Context와 사용자 요청을 기준으로 작업하세요.\n"
                  "[End Frontend Domain RAG]")
        if count(system, user + notice) <= rag_limit:
            prompt = user + notice
            tokens = count(system, prompt)
    metadata = {
        "status": status, "counter": kind, "base_prompt_tokens": base_tokens,
        "prompt_tokens": tokens, "input_limit": limit,
        "rag_input_limit": rag_limit,
        "rag_headroom": max(0, rag_headroom),
        "reserved_output_tokens": num_predict, "safety_tokens": SAFETY_TOKENS,
        "retrieved_count": len(results), "injected_count": len(selected),
        "sources": [r["source"] for r in results],
        "injected_sources": [r["source"] for r in selected],
        "injected_headings": [r["heading"] for r in selected],
        "injected_scores": [r["score"] for r in selected],
        "budget_exceeded": tokens > limit,
    }
    return prompt, metadata


class DBPromptBudgetError(ValueError):
    """필수 DB 입력이 예산을 초과하면 불완전한 Prompt 전송을 중단한다."""

    def __init__(self, metadata):
        self.metadata = metadata
        super().__init__(
            f"DB 필수 Prompt 예산 부족: {metadata['base_prompt_tokens']} tokens > "
            f"입력 한도 {metadata['input_limit']} tokens "
            f"(출력 예약={metadata['reserved_output_tokens']}, "
            f"안전 여유={metadata['safety_tokens']}, counter={metadata['counter']}). "
            "요구사항·Rules·Issue·직전 산출물·Handoff·Project Context를 자르지 않고 전송을 중단합니다."
        )


def pack_db_rag(system, user, results, *, model, num_ctx, num_predict,
                counter=None, rag_headroom=128, format_context=None, empty_context=None):
    """필수 입력 전체를 보존하고 선택적 DB RAG만 완전한 chunk 단위로 주입한다."""
    count, kind = prompt_counter(model) if counter is None else (counter, "test_counter")
    formatter = format_context or format_db_context
    base_tokens = count(system, user)
    limit = num_ctx - num_predict - SAFETY_TOKENS
    optional_limit = limit - max(0, rag_headroom)
    metadata = {
        "counter": kind, "context_size": num_ctx,
        "reserved_output_tokens": num_predict, "safety_tokens": SAFETY_TOKENS,
        "input_limit": limit, "rag_input_limit": optional_limit,
        "rag_headroom": max(0, rag_headroom),
        "base_prompt_tokens": base_tokens, "prompt_tokens": base_tokens,
        "remaining_tokens": limit - base_tokens,
        "budget_exceeded": base_tokens > limit,
        "retrieved_count": len(results), "injected_count": 0,
        "sources": [r["source"] for r in results], "injected_sources": [],
    }
    if metadata["budget_exceeded"]:
        raise DBPromptBudgetError(metadata)

    prompt, tokens, selected = user, base_tokens, []
    for result in results[:3]:
        candidate = (
            user + "\n\n[Domain RAG — general technical guidance]\n"
            + formatter([*selected, result]) + "\n[End Domain RAG]"
        )
        candidate_tokens = count(system, candidate)
        if candidate_tokens <= optional_limit:
            selected.append(result)
            prompt, tokens = candidate, candidate_tokens
    notice_injected = False
    if not results:
        candidate = (
            user + "\n\n[Domain RAG — general technical guidance]\n"
            + (empty_context if empty_context is not None else formatter([])) + "\n[End Domain RAG]"
        )
        candidate_tokens = count(system, candidate)
        if candidate_tokens <= optional_limit:
            prompt, tokens, notice_injected = candidate, candidate_tokens, True
    metadata.update(
        prompt_tokens=tokens, remaining_tokens=limit - tokens,
        injected_count=len(selected), injected_sources=[r["source"] for r in selected],
        extra_headroom_met=limit - tokens >= max(0, rag_headroom),
        notice_injected=notice_injected,
    )
    return prompt, metadata


def prepare_tokenizer():
    data = urllib.request.urlopen(TOKENIZER_URL, timeout=60).read()
    if hashlib.sha256(data).hexdigest() != TOKENIZER_SHA256:
        raise ValueError("Downloaded tokenizer checksum mismatch")
    TOKENIZER_PATH.parent.mkdir(parents=True, exist_ok=True)
    pending = TOKENIZER_PATH.with_suffix(".pending")
    pending.write_bytes(data)
    pending.replace(TOKENIZER_PATH)
    print(f"Qwen tokenizer ready: {TOKENIZER_PATH}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepare-tokenizer", action="store_true", required=True)
    parser.parse_args()
    prepare_tokenizer()
