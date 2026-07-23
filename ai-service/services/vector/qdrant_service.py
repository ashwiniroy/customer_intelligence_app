from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct
)


class QdrantService:

    def __init__(self):
        self.client = QdrantClient(
            host="localhost",
            port=6333
        )

    def create_collection(self):

        collections = self.client.get_collections().collections

        exists = any(c.name == "reviews" for c in collections)

        if not exists:

            self.client.create_collection(
                collection_name="reviews",
                vectors_config=VectorParams(
                    size=384,
                    distance=Distance.COSINE
                )
            )

            print("✅ reviews collection created")

        else:

            print("✅ reviews collection already exists")

    def insert_review(self, review_id, vector, payload):

        self.client.upsert(
            collection_name="reviews",
            points=[
                PointStruct(
                    id=review_id,
                    vector=vector,
                    payload=payload
                )
            ]
        )

    def search_reviews(
        self,
        query_vector,
        limit=5
    ):

     results = self.client.query_points(
        collection_name="reviews",
        query=query_vector,
        limit=limit
     )

     return results.points
    

from qdrant_client.models import PointStruct


def insert_review(
    self,
    review_id: int,
    vector: list,
    payload: dict
):
    self.client.upsert(
        collection_name="reviews",
        points=[
            PointStruct(
                id=review_id,
                vector=vector,
                payload=payload
            )
        ]
    )