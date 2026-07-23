from fastapi import APIRouter

from services.ingestion.ingestion_service import IngestionService

router = APIRouter(
    prefix="/api/ingest",
    tags=["Ingestion"]
)

service = IngestionService()

@router.post("/reviews")
def ingest_reviews():
    return service.ingest_reviews()