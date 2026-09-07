import json
import os
import tempfile
import unittest
from pathlib import Path

import agents.nodes as nodes
from main import save_llm_metrics


class FakeResponse:
    def __init__(self, content=" generated result ", metadata=None):
        self.content = content
        if metadata is not None:
            self.response_metadata = metadata


class FakeLlm:
    def __init__(self, metadata=None, model="fallback-model"):
        self.model = model
        self.num_ctx = 12288
        self.num_predict = 2048
        self.metadata = metadata

    def invoke(self, messages):
        assert len(messages) == 2
        return FakeResponse(metadata=self.metadata)


def complete_metadata(**overrides) -> dict:
    metadata = {
        "model": "metadata-model",
        "model_name": "metadata-model-name",
        "done_reason": "stop",
        "total_duration": 3_550_600_000,
        "load_duration": 120_000_000,
        "prompt_eval_count": 9594,
        "prompt_eval_duration": 973_500_000,
        "eval_count": 963,
        "eval_duration": 2_498_800_000,
    }
    metadata.update(overrides)
    return metadata


def invoke_metric(metadata=None, model="fallback-model") -> tuple[str, dict]:
    sink = []
    result = nodes.invoke_agent(
        FakeLlm(metadata=metadata, model=model),
        "SYSTEM_PROMPT_SECRET",
        "USER_PROMPT_SECRET",
        metric_context={
            "agent": "frontend",
            "mode": "integration_fix",
            "call_index": 1,
        },
        metrics_sink=sink,
    )
    return result, sink[0]


def frontend_state() -> dict:
    return {
        "user_request": "회원가입 화면 구현",
        "required_agents": ["backend", "frontend"],
        "project_plan": "Frontend 계획",
        "backend_result": "Backend 결과",
        "frontend_result": "PREVIOUS_FRONTEND_RESULT",
        "frontend_validation": {"status": "PASS", "issues": []},
        "frontend_fix_count": 0,
        "integration_validation": {"status": "NOT_RUN", "issues": []},
        "integration_fix_count": 0,
        "llm_metrics": [],
    }


def run_frontend_with_metric_capture(state: dict) -> dict:
    original_invoke_agent = nodes.invoke_agent

    def fake_invoke(
        llm,
        system_prompt,
        user_prompt,
        metric_context=None,
        metrics_sink=None,
    ):
        del llm, system_prompt, user_prompt
        metrics_sink.append(dict(metric_context))
        return "UPDATED_FRONTEND_RESULT"

    nodes.invoke_agent = fake_invoke
    try:
        return nodes.frontend_agent(state)
    finally:
        nodes.invoke_agent = original_invoke_agent


def test_metadata_fields_and_nanoseconds_are_recorded() -> None:
    result, metric = invoke_metric(complete_metadata())
    assert result == "generated result"
    assert metric["model"] == "metadata-model"
    assert metric["done_reason"] == "stop"
    assert metric["prompt_eval_count"] == 9594
    assert metric["eval_count"] == 963
    assert metric["context_size"] == 12288
    assert metric["num_predict"] == 2048
    assert metric["total_duration_ns"] == 3_550_600_000
    assert metric["total_seconds"] == 3.5506
    assert metric["load_seconds"] == 0.12
    assert metric["prompt_eval_seconds"] == 0.9735
    assert metric["eval_seconds"] == 2.4988
    assert isinstance(metric["wall_seconds"], float)
    assert metric["wall_seconds"] >= 0


def test_model_fallback_order() -> None:
    _, from_model = invoke_metric(complete_metadata())
    _, from_model_name = invoke_metric(
        complete_metadata(model=None, model_name="name-model")
    )
    _, from_llm = invoke_metric(
        complete_metadata(model=None, model_name=None),
        model="llm-model",
    )
    assert from_model["model"] == "metadata-model"
    assert from_model_name["model"] == "name-model"
    assert from_llm["model"] == "llm-model"


def test_missing_metadata_keeps_nullable_fields_and_string_result() -> None:
    result, metric = invoke_metric(None)
    assert result == "generated result"
    for key in (
        "done_reason",
        "prompt_eval_count",
        "eval_count",
        "total_duration_ns",
        "total_seconds",
        "load_duration_ns",
        "load_seconds",
        "prompt_eval_duration_ns",
        "prompt_eval_seconds",
        "eval_duration_ns",
        "eval_seconds",
    ):
        assert metric[key] is None


def test_frontend_modes_sequence_and_state_list_immutability() -> None:
    initial_state = frontend_state()
    original_metrics = initial_state["llm_metrics"]
    initial_result = run_frontend_with_metric_capture(initial_state)
    assert original_metrics == []
    assert initial_result["llm_metrics"] == [{
        "agent": "frontend",
        "mode": "initial",
        "call_index": 1,
    }]

    integration_state = dict(initial_state)
    integration_state.update(initial_result)
    integration_state["frontend_validation"] = {"status": "PASS", "issues": []}
    integration_state["integration_validation"] = {
        "status": "FAIL",
        "issues": [{
            "rule": "SUCCESS_STATUS_MISMATCH",
            "target_agent": "frontend",
        }],
    }
    integration_result = run_frontend_with_metric_capture(integration_state)
    assert [item["call_index"] for item in integration_result["llm_metrics"]] == [1, 2]
    assert integration_result["llm_metrics"][1]["mode"] == "integration_fix"
    assert integration_result["integration_fix_count"] == 1

    validator_state = dict(integration_state)
    validator_state.update(integration_result)
    validator_state["frontend_validation"] = {
        "status": "FAIL",
        "issues": [{"rule": "UNSAFE_CATCH_ERROR_ACCESS"}],
    }
    validator_result = run_frontend_with_metric_capture(validator_state)
    assert [item["call_index"] for item in validator_result["llm_metrics"]] == [1, 2, 3]
    assert validator_result["llm_metrics"][2]["mode"] == "validator_fix"
    assert validator_result["frontend_fix_count"] == 1
    assert validator_result["integration_fix_count"] == 1


def test_metrics_json_is_saved_without_sensitive_content() -> None:
    metrics = [{
        "call_index": 1,
        "agent": "frontend",
        "mode": "initial",
        "prompt_eval_count": 100,
        "eval_count": 20,
    }]
    previous_directory = Path.cwd()
    with tempfile.TemporaryDirectory() as temporary_directory:
        os.chdir(temporary_directory)
        try:
            output_path = save_llm_metrics(metrics)
            payload = json.loads(output_path.read_text(encoding="utf-8"))
        finally:
            os.chdir(previous_directory)

    assert payload["schema_version"] == 1
    assert payload["call_count"] == 1
    assert payload["calls"] == metrics
    serialized = json.dumps(payload, ensure_ascii=False)
    assert "SYSTEM_PROMPT_SECRET" not in serialized
    assert "USER_PROMPT_SECRET" not in serialized
    assert "user_request" not in serialized
    assert "system_prompt" not in serialized
    assert "user_prompt" not in serialized


def load_tests(loader, tests, pattern):
    del loader, tests, pattern
    suite = unittest.TestSuite()
    for name, value in sorted(globals().items()):
        if name.startswith("test_") and callable(value):
            suite.addTest(unittest.FunctionTestCase(value))
    return suite


if __name__ == "__main__":
    unittest.main(verbosity=2)
