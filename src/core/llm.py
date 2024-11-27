from abc import ABC, abstractmethod
from typing import Optional, Dict

class BaseLLM(ABC):
    """추상 기본 클래스 - 다양한 LLM 구현을 위한 인터페이스"""
    
    @abstractmethod
    async def generate(self, prompt: str, context: Optional[str] = None) -> str:
        """LLM 응답 생성"""
        pass

    @abstractmethod
    async def get_embedding(self, text: str) -> list:
        """텍스트 임베딩 생성"""
        pass

class LLMFactory:
    """LLM 구현체를 생성하는 팩토리 클래스"""
    
    @staticmethod
    def create(provider: str, config: Dict) -> BaseLLM:
        """
        provider에 따라 적절한 LLM 구현체를 반환
        예: 'openai', 'anthropic', 'bedrock' 등
        """
        # 추후 구현
        pass 