from dataclasses import dataclass


@dataclass
class RCAResult:
    root_cause: str
    explanation: str
    fix: str
    confidence: float
