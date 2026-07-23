from services.nlp.sentiment_service import SentimentService
from services.embedding.embedding_service import EmbeddingService
from services.vector.qdrant_service import QdrantService
from models.response import ReviewAnalysisResponse


class ReviewService:

    def __init__(self):

        self.sentiment = SentimentService()

        self.embedding = EmbeddingService()

        self.qdrant = QdrantService()

    def analyze_review(self, request):

        sentiment = self.sentiment.analyze(request.review)

        embedding = self.embedding.generate_embedding(request.review)

        payload = {

            "customer": request.customer,

            "product": request.product,

            "rating": request.rating,

            "review": request.review,

            "sentiment": sentiment["label"]

        }

        self.qdrant.insert_review(

            review_id=request.review_id,

            vector=embedding,

            payload=payload

        )

        return ReviewAnalysisResponse(

            sentiment=sentiment["label"],

            confidence=sentiment["score"],

            summary=request.review,

            embeddings=embedding

        )