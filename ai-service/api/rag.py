from fastapi import APIRouter

from models.rag import (
    RAGRequest,
    RAGResponse
)


router = APIRouter(
    prefix="/rag",
    tags=["RAG"]
)


# Temporary instance
# Later we will move this to dependency injection

from core.dependencies import rag_service



@router.post("/query")
async def query_rag(
        request: RAGRequest
):

    result = rag_service.ask(
        request.question
    )


    return RAGResponse(
        answer=result["answer"]
    )