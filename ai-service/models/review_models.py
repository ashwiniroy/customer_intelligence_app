from pydantic import BaseModel


class ReviewRequest(BaseModel):

    review_id: int

    customer: str

    product: str

    rating: int

    review: str