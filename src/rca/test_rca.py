from src.rca.rca_engine import RCAEngine
from src.rca.llm import LocalLLM   # or whatever LLM wrapper you created

def test_rca():
    llm = LocalLLM()   # explicitly create LLM
    engine = RCAEngine(llm=llm)

    logs = [
        "ERROR Failed to connect to database",
        "WARN Database retry attempt 1",
        "INFO Connection successful",
        "ERROR API timeout",
        "WARN Slow response detected"
    ]

    result = engine.analyze(logs)

    print("\n===== RCA RESULT =====")
    print(result)

if __name__ == "__main__":
    test_rca()
