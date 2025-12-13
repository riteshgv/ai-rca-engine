# src/rca/llm_reasoner.py

from transformers import pipeline

class LLMReasoner:
    def __init__(self, model_name="distilbert/distilgpt2"):
        """
        Lightweight local model (no internet, no API key)
        Replace later with any enterprise LLM.
        """
        self.generator = pipeline("text-generation", model=model_name)

    def generate_rca(self, context):
        prompt = (
            "You are an expert Root Cause Analysis system.\n"
            "Given the following log context, identify:\n"
            "1. Most probable root cause\n"
            "2. Why it occurred\n"
            "3. Recommended fix\n\n"
            f"Logs:\n{context}\n\n"
            "RCA:"
        )
        result = self.generator(prompt, max_length=200, num_return_sequences=1)
        return result[0]["generated_text"]

