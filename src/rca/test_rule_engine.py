from src.rca.rule_engine import rule_based_rca

def test_rule_engine():
    logs = [
        "ERROR Failed to connect to database",
        "WARN Database retry attempt 1",
        "INFO Connection successful"
    ]

    result = rule_based_rca(logs)

    assert result is not None
    assert "database" in result["root_cause"].lower()

    print("Rule-based RCA result:")
    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    test_rule_engine()

