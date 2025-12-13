from src.rca.rule_engine import rule_based_rca
from src.rca.prompt_builder import build_rca_prompt
from src.rca.rca_schema import RCAResult

class RCAEngine:

    def __init__(self, llm):
        self.llm = llm

    def analyze(self, log_chunks: list[str]) -> RCAResult:
        rule_result = rule_based_rca(log_chunks)

        if rule_result:
            return RCAResult(**rule_result)

        prompt = build_rca_prompt(log_chunks)
        response = self.llm.generate(prompt)

        return self._parse_response(response)

    def _parse_response(self, text: str) -> RCAResult:
        lines = text.split("\n")

        return RCAResult(
            root_cause=lines[0].replace("Root Cause:", "").strip(),
            reason=lines[1].replace("Why it occurred:", "").strip(),
            fix=lines[2].replace("Recommended Fix:", "").strip(),
            confidence=float(lines[3].split(":")[-1].strip())
        )
