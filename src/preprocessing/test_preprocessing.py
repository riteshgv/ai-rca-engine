import json
from src.preprocessing.chunker import chunk_logs
from src.preprocessing.embedder import generate_embeddings
from src.preprocessing.semantic_search import SemanticSearchIndex

# Load normalized logs
logs = json.load(open("normalized_logs.json", "r"))

# 1. Chunk logs
chunks = chunk_logs(logs, max_chunk_size=5)

# 2. Embeddings
embs = generate_embeddings(chunks)

# 3. Build index
index = SemanticSearchIndex(embedding_dim=embs.shape[1])
index.add(embs)

# 4. Test search
query = ["database connection error occurred"]
query_emb = generate_embeddings([ [{"message": query[0]}] ])

distances, results = index.search(query_emb, top_k=3)

print(distances, results)

