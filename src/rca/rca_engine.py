class RCAEngine:
    def __init__(self, llm):
        self.llm = llm

    def analyze(self, current_logs, similar_logs):
        """
        current_logs: str
        similar_logs: chromadb query result
        """

        # Safely extract distances
        raw_distances = similar_logs.get("distances", [])

        # Chroma returns List[List[float]]
        if raw_distances and isinstance(raw_distances[0], list):
            distances = raw_distances[0]
        else:
            distances = []

        confidence = self._calculate_confidence(distances)

        prompt = self._build_prompt(current_logs, similar_logs)

        rca_text = self.llm.generate(prompt)

        return {
            "rca": rca_text,
            "confidence": confidence
        }

    def _calculate_confidence(self, distances):
        if not distances:
            return 0.0

        # distances are similarity → lower = closer
        avg_distance = sum(distances) / len(distances)

        # Normalize to confidence score
        confidence = max(0.0, min(1.0, 1 - avg_distance))
        return round(confidence, 2)

    def _build_prompt(self, current_logs, similar_logs):
        docs = similar_logs.get("documents", [[]])[0]

        if docs:
            context = "\n".join(docs)
        else:
            context = "No similar historical incidents available."

        return f"""
            You are an experienced Site Reliability Engineer.

            Analyze the incident logs and provide Root Cause Analysis.

            Incident Logs:
            {current_logs}

            Similar Past Incidents:
            {context}

            Respond STRICTLY in the following format:

            Root Cause:
            <one sentence>

            Why it happened:
            <2–3 lines>

            Recommended Fix:
            <clear actionable steps>
            """

