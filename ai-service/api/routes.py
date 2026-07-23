from fastapi import APIRouter

from api.health import router as health_router
from api.review import router as review_router
from api.search import router as search_router

router = APIRouter()

router.include_router(
    health_router,
    prefix="/api",
    tags=["Health"]
)

router.include_router(
    review_router,
    prefix="/api",
    tags=["Review Analysis"]
)

router.include_router(

    search_router,

    prefix="/api",

    tags=["Semantic Search"]

)