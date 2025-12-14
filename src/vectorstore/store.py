import chromadb


class VectorStore:
    def __init__(self, path=".chroma"):
        self.client = chromadb.Client(
            chromadb.config.Settings(persist_directory=path)
        )
        self.collection = self.client.get_or_create_collection("logs")

    def add(self, texts, embeddings):
        self.collection.add(
            documents=texts,
            embeddings=embeddings,
            ids=[str(i) for i in range(len(texts))]
        )

    def search(self, query, embed_fn, k=5):
        embedding = embed_fn([query])[0]
        return self.collection.query(
            query_embeddings=[embedding],
            n_results=k
        )
