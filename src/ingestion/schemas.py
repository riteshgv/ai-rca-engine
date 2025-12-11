from dataclasses import dataclass

@dataclass
class NormalizedLog:
    timestamp: str
    level: str
    source: str
    message: str

