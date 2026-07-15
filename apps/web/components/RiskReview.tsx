"use client";
import { useState } from "react";
import { assessTransfer, RiskAssessment } from "../lib/api";

export function RiskReview() {
  const [result, setResult] = useState<RiskAssessment>();
  const [loading, setLoading] = useState(false);
  async function review() { setLoading(true); try { setResult(await assessTransfer({ recipientId: "new-recipient", amount: 8000 })); } finally { setLoading(false); } }
  return <section className="rounded-2xl bg-white p-6 shadow-sm"><h2 className="text-2xl font-bold">Send money safely</h2><p className="mt-2 text-slate-600">We will explain anything unusual before you send.</p><button onClick={review} disabled={loading} className="mt-5 rounded-xl bg-safety px-6 py-4 text-lg font-semibold text-white">{loading ? "Checking..." : "Review a transfer"}</button>{result && <div className="mt-5 rounded-xl border border-amber-300 bg-amber-50 p-4" role="status"><p className="font-bold capitalize">{result.level} risk - score {result.score}/100</p><p className="mt-2">{result.guidance}</p><ul className="mt-2 list-disc pl-5">{result.reasons.map(reason => <li key={reason}>{reason}</li>)}</ul></div>}</section>;
}
