import requests

from config.settings import settings
from services.embedding.embedding_service import EmbeddingService
from services.vector.qdrant_service import QdrantService


class IngestionService:

    def __init__(self):
        self.embedding = EmbeddingService()
        self.qdrant = QdrantService()

    def ingest_reviews(self):

        response = requests.get(settings.REVIEW_API)

        print("Status:", response.status_code)
        print("URL:", response.url)
        print("Headers:", response.headers.get("Content-Type"))
        print("Body:")
        print(response.text)

        reviews = response.json()

        count = 0

        for review in reviews:

            vector = self.embedding.generate_embedding(
                review["reviewDescription"]
            )

            payload = {
                "review": review["reviewDescription"],
                "title": review["reviewTitle"],
                "rating": review["rating"],
                "customer": review["customerName"],
                "product": review["product"],
                "category": review["category"]
            }

            self.qdrant.insert_review(
                review["id"],
                vector,
                payload
            )

            count += 1

        return {
            "status": "success",
            "ingested": count
        }