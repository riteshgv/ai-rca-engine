def build_rca_prompt(log_chunks: list[str]) -> str:
    context = "\n".join(log_chunks)

    return f"""
You are a Site Reliability Engineer performing Root Cause Analysis.

Rules:
- Do NOT repeat logs
- Do NOT generate new logs
- Respond ONLY in the following format

Root Cause:
Why it occurred:
Recommended Fix:
Confidence (0-1):

Logs:
{context}
"""

