from transformers import pipeline


class SentimentService:

    def __init__(self):

        self.pipeline = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    def analyze(self, text):

        result = self.pipeline(text)[0]

        return {
            "label": result["label"],
            "score": float(result["score"])
        }