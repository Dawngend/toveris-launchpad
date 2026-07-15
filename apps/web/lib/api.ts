const API_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";
export type RiskAssessment = { score: number; level: "low" | "medium" | "high"; reasons: string[]; guidance: string };
export async function assessTransfer(input: { recipientId: string; amount: number }): Promise<RiskAssessment> {
  const response = await fetch(`${API_URL}/v1/transfers/assess`, { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify(input) });
  if (!response.ok) throw new Error("We could not check this transfer right now.");
  return response.json();
}
