class PromptBuilder:


    def build_review_prompt(
            self,
            question,
            context
    ):

        prompt = f"""
You are an AI assistant that analyzes customer reviews.

Use only the provided review context.

Context:
{context}


Question:
{question}


Provide a clear and concise answer.
"""

        return prompt