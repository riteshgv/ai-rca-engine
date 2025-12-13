from dataclasses import dataclass

@dataclass
class RCAResult:
    root_cause: str
    reason: str
    fix: str
    confidence: float

