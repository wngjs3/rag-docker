from typing import List, Optional
from src.config import settings

class EmbeddingService:
    def __init__(self, llm_client):
        self.llm_client = llm_client
    
    async def create_embedding(self, text: str) -> List[float]:
        """텍스트의 임베딩을 생성"""
        return await self.llm_client.get_embedding(text)
    
    async def create_batch_embeddings(self, texts: List[str]) -> List[List[float]]:
        """여러 텍스트의 임베딩을 배치로 생성"""
        embeddings = []
        for text in texts:
            embedding = await self.create_embedding(text)
            embeddings.append(embedding)
        return embeddings 