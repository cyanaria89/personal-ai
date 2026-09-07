export interface SignupPayload {
  loginId: string;
  password: string;
  memberName: string;
}

export interface SignupResult {
  id: number;
  loginId: string;
  memberName: string;
}

export async function signup(payload: SignupPayload): Promise<SignupResult> {
  const response = await fetch("/api/members/signup", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!response.ok) {
    throw new Error("회원가입에 실패했습니다.");
  }

  return response.json() as Promise<SignupResult>;
}
