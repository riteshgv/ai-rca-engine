# src/rca/rca_engine.py

from src.preprocessing.chunker import chunk_logs
from src.embedding.embedder import LogEmbedder
from src.embedding.vector_store import VectorStore
from src.rca.llm_reasoner import LLMReasoner

class RCAEngine:
    def __init__(self):
        self.embedder = LogEmbedder()
        self.store = VectorStore()
        self.reasoner = LLMReasoner()

    def analyze_logs(self, raw_logs):
        # Step 1: chunk logs
        chunks = chunk_logs(raw_logs, 3)

        # Step 2: embed chunks
        vectors = self.embedder.embed(chunks)

        # Step 3: store chunks into vector DB
        ids = [f"chunk_{i}" for i in range(len(chunks))]
        metadata = [{"text": c} for c in chunks]
        self.store.add_embeddings(ids, vectors, metadata)

        # Step 4: find top similar incidents
        joined_logs = "\n".join(raw_logs)
        results = self.store.search(joined_logs, self.embedder.embed, n=3)

        # Step 5: select best match
        best_texts = [m["text"] for m in results["metadatas"][0]]

        # Step 6: AI reasoning
        context = "\n".join(best_texts)
        rca_result = self.reasoner.generate_rca(context)

        return {
            "similar_chunks": best_texts,
            "root_cause_analysis": rca_result
        }

