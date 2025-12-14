from src.embedding.embedder import embed_texts


class IncrementalRCA:
    def __init__(self, engine):
        self.engine = engine

    def process_window(self, window, vector_store):
        """
        window: List[str] (raw log lines)
        """

        # 1️⃣ Join raw log lines FIRST
        query_text = "\n".join(window)

        # 2️⃣ Extract deterministic signal
        def extract_signal(log_text):
            text = log_text.lower()
            if "timeout" in text:
                return "Timeout or slow downstream dependency"
            if "connection refused" in text or "failed to connect" in text:
                return "Connectivity or database issue"
            if "out of memory" in text:
                return "Memory exhaustion"
            return "Unknown issue"

        signal = extract_signal(query_text)

        # 3️⃣ Enrich query text with signal
        query_text = f"Signal: {signal}\nLogs:\n{query_text}"

        # 4️⃣ Vector search
        search_result = vector_store.search(
            query=query_text,
            embed_fn=embed_texts,
            k=5
        )

        # 5️⃣ Guard: no historical evidence
        if not search_result.get("documents") or not search_result["documents"][0]:
            return {
                "rca": "No similar historical incidents found yet.",
                "confidence": 0.0
            }

        # 6️⃣ Call RCA engine
        rca_result = self.engine.analyze(
            query_text,
            search_result
        )

        return rca_result
