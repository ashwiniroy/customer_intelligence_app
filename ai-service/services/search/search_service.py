from services.embedding.embedding_service import EmbeddingService
from services.vector.qdrant_service import QdrantService


class SearchService:

    def __init__(self):

        self.embedding = EmbeddingService()

        self.qdrant = QdrantService()

    def search(self, query):

        vector = self.embedding.generate(query)

        results = self.qdrant.search_reviews(vector)

        return results