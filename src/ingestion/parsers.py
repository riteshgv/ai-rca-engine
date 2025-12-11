import re
from .schemas import NormalizedLog

# Regex patterns for various log styles
PATTERNS = [
    # Example: "2025-01-12 10:15:22 ERROR Something broke"
    re.compile(r"(?P<timestamp>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (?P<level>[A-Z]+) (?P<message>.*)"),

    # Example: "2025-01-12T10:20:33Z [ERROR] [MySQL] Message..."
    re.compile(r"(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z) \[(?P<level>\w+)\] \[(?P<source>\w+)\] (?P<message>.*)")
]


def parse_line(line: str):
    for pattern in PATTERNS:
        match = pattern.match(line)
        if match:
            data = match.groupdict()
            return NormalizedLog(
                timestamp=data.get("timestamp", ""),
                level=data.get("level", "").upper(),
                source=data.get("source", "UNKNOWN"),
                message=data.get("message", "")
            )
    return None  # Line didn't match known patterns

