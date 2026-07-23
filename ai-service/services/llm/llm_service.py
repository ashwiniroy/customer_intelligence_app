import ollama


class LLMService:

    def __init__(self):
        self.model = "llama3:8b"

    def generate(self, prompt: str):

        response = ollama.chat(
            model=self.model,
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an AI assistant specialized in "
                        "customer review analysis."
                    ),
                },
                {
                    "role": "user",
                    "content": prompt,
                },
            ],
        )

        return {
            "answer": response["message"]["content"]
        }