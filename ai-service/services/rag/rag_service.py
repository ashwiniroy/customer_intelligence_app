from services.prompts.prompt_builder import PromptBuilder
from services.llm.llm_service import LLMService


class RAGService:


    def __init__(
        self,
        qdrant_service,
        embedding_service
    ):

        self.qdrant = qdrant_service
        self.embedding = embedding_service

        self.prompt_builder = PromptBuilder()

        self.llm = LLMService()



    def ask(
        self,
        question
    ):


        # 1. Convert question to vector

        query_vector = (
            self.embedding
            .generate_embedding(question)
        )


        # 2. Search similar reviews

        results = (
            self.qdrant
            .search_reviews(
                query_vector
            )
        )


        # 3. Build context

        context = "\n".join(
            [
                item.payload["review"]
                for item in results
            ]
        )


        # 4. Create prompt

        prompt = (
            self.prompt_builder
            .build_review_prompt(
                question,
                context
            )
        )


        # 5. Send to LLM

        response = (
            self.llm
            .generate(prompt)
        )


        return response