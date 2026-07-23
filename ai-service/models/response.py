from pydantic import BaseModel
from typing import List


class ReviewAnalysisResponse(BaseModel):

    sentiment: str

    confidence: float

    summary: str

    embeddings: List[float]

    keywords: List[str] = []

    entities: List[str] = []