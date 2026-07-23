from fastapi import APIRouter

from models.review_models import ReviewRequest

from services.review_service import ReviewService

router = APIRouter()

service = ReviewService()


@router.post("/analyze-review")
async def analyze_review(request: ReviewRequest):

    return service.analyze_review(request)