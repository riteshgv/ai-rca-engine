import argparse

from src.vectorstore.store import VectorStore
from src.embedding.embedder import embed_texts
from src.streaming.window import build_windows
from src.rca.rca_engine import RCAEngine
from src.rca.incremental_rca import IncrementalRCA
# from src.rca.llm.local_llm import LocalLLM
from src.rca.llm import LocalLLM



def read_logs(file_path):
    with open(file_path, "r") as f:
        return [line.strip() for line in f.readlines() if line.strip()]


def main():
    parser = argparse.ArgumentParser(description="AI RCA Engine")
    parser.add_argument("--file", required=True)
    parser.add_argument("--stream", action="store_true")
    args = parser.parse_args()

    logs = read_logs(args.file)

    store = VectorStore()
    engine = RCAEngine(llm=LocalLLM())

    if args.stream:
        windows = build_windows(logs, window_minutes=3)
        inc = IncrementalRCA(engine)

        for i, w in enumerate(windows, 1):
            result = inc.process_window(w, store)
            print(f"\n===== Window {i} =====")
            print(result)
    else:
        result = engine.run_full_rca(logs, store)
        print(result)
