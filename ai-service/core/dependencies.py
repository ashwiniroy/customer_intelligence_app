from services.rag.rag_service import RAGService
from services.vector.qdrant_service import QdrantService
from services.embedding.embedding_service import EmbeddingService



qdrant = QdrantService()

embedding = EmbeddingService()



rag_service = RAGService(
    qdrant,
    embedding
)