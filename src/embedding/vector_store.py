# src/embedding/vector_store.py

import chromadb

class VectorStore:
    def __init__(self, collection_name="log_embeddings"):
        # NEW API — no Settings() needed
        self.client = chromadb.PersistentClient(path="chroma_db")
        self.collection = self.client.get_or_create_collection(
            name=collection_name,
            metadata={"hnsw:space": "cosine"}   # cosine similarity for embeddings
        )

    def add_embeddings(self, ids, embeddings, metadata):
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            metadatas=metadata
        )

    def search(self, query_text, embed_fn, n=5):
        query_embedding = embed_fn([query_text])[0]
        result = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n
        )
        return result
