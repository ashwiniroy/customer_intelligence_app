from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health():
    return {
        "status": "healthy",
        "service": "Review Analysis AI Service",
        "version": "1.0.0"
    }