from fastapi import FastAPI

from api.review import router as review_router
from api.search import router as search_router
from api.rag import router as rag_router
from api.ingestion import router as review_ingestion_router

app = FastAPI(
    title="Review Analysis AI Service"
)

app.include_router(review_router, prefix="/api")
app.include_router(search_router, prefix="/api")
app.include_router(rag_router, prefix="/api")
app.include_router(review_ingestion_router, prefix="/api")


@app.get("/")
def home():
    return {"message": "AI Service Running"}