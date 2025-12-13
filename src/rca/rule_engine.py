def rule_based_rca(logs: list[str]) -> dict | None:
    text = " ".join(logs).lower()

    if "database" in text and "failed" in text:
        return {
            "root_cause": "Database connectivity issue",
            "reason": "Initial connection failures caused retries and delays",
            "fix": "Check DB availability, network latency, and connection pool limits",
            "confidence": 0.75
        }

    if "timeout" in text:
        return {
            "root_cause": "Service timeout",
            "reason": "Upstream dependency responded slowly or was overloaded",
            "fix": "Increase timeout, optimize service, or add circuit breakers",
            "confidence": 0.70
        }

    return None

