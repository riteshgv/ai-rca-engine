import faiss
import numpy as np

class SemanticSearchIndex:

    def __init__(self, embedding_dim):
        self.index = faiss.IndexFlatL2(embedding_dim)
        self.vectors = []

    def add(self, embeddings):
        self.index.add(embeddings)
        self.vectors.append(embeddings)

    def search(self, query_embedding, top_k=3):
        distances, indices = self.index.search(query_embedding, top_k)
        return distances, indices

