# src/rca/test_rca.py

from src.rca.rca_engine import RCAEngine

def test_rca():
    sample_logs = [
        "2024-01-20 10:01:02 ERROR Failed to connect to database",
        "2024-01-20 10:01:05 WARN Retry attempt 1",
        "2024-01-20 10:01:06 ERROR Database timeout",
        "2024-01-20 11:03:22 INFO Server recovered"
    ]

    engine = RCAEngine()
    result = engine.analyze_logs(sample_logs)

    print("\n========= Top Similar Log Chunks =========")
    for c in result["similar_chunks"]:
        print(c)
    print("\n========= RCA Result =========")
    print(result["root_cause_analysis"])

if __name__ == "__main__":
    test_rca()

