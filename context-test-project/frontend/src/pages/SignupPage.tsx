import { FormEvent, useState } from "react";

import { signup } from "../api/authApi";

export function SignupPage() {
  const [loginId, setLoginId] = useState("");
  const [password, setPassword] = useState("");
  const [memberName, setMemberName] = useState("");
  const [message, setMessage] = useState("");

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setMessage("");

    try {
      await signup({ loginId, password, memberName });
      setMessage("회원가입이 완료되었습니다.");
    } catch (error: unknown) {
      setMessage(error instanceof Error ? error.message : "회원가입에 실패했습니다.");
    }
  }

  return (
    <main>
      <h1>회원가입</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="loginId">아이디</label>
        <input id="loginId" value={loginId} onChange={(event) => setLoginId(event.target.value)} required />

        <label htmlFor="password">비밀번호</label>
        <input id="password" type="password" value={password} onChange={(event) => setPassword(event.target.value)} required />

        <label htmlFor="memberName">이름</label>
        <input id="memberName" value={memberName} onChange={(event) => setMemberName(event.target.value)} required />

        <button type="submit">가입하기</button>
      </form>
      {message && <p role="status">{message}</p>}
    </main>
  );
}
