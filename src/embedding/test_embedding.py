# src/embedding/test_embedding.py

from src.preprocessing.chunker import chunk_logs
from src.embedding.embedder import LogEmbedder
from src.embedding.vector_store import VectorStore

def get_sample_logs():
    return [
        "2024-01-20 10:01:02 ERROR Failed to connect to database",
        "2024-01-20 10:01:05 WARN Database retry attempt 1",
        "2024-01-20 10:01:06 INFO Connection successful",
        "2024-01-20 11:03:22 ERROR API timeout",
        "2024-01-20 11:03:30 WARN Slow response detected",
    ]

def test_embedding_pipeline():
    logs = get_sample_logs()
    chunks = chunk_logs(logs,window_size=2)
    
    embedder = LogEmbedder()
    vectors = embedder.embed(chunks)

    store = VectorStore()
    metadata = [{"text": c} for c in chunks]
    ids = [f"chunk_{i}" for i in range(len(chunks))]

    store.add_embeddings(ids, vectors, metadata)

    # Test search
    query = "database error"
    search_result = store.search(query, embedder.embed, n=3)
    print("Query:", query)
    print("Search result:", search_result)

if __name__ == "__main__":
    test_embedding_pipeline()

