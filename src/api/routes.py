from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from src.core.llm import LLMFactory
from src.db.opensearch_client import OpenSearchClient

router = APIRouter()

class QueryRequest(BaseModel):
    question: str
    context: Optional[str] = None

class QueryResponse(BaseModel):
    answer: str
    sources: Optional[List[str]] = None

@router.post("/query", response_model=QueryResponse)
async def query(request: QueryRequest):
    try:
        # OpenSearch 클라이언트 초기화
        opensearch = OpenSearchClient()
        
        # LLM 클라이언트 초기화 (구체적인 구현은 선택한 LLM에 따라 달라짐)
        llm = LLMFactory.create("your_chosen_provider", {})
        
        # 질문의 임베딩 생성
        question_embedding = await llm.get_embedding(request.question)
        
        # 유사한 문서 검색
        similar_docs = await opensearch.search_similar(question_embedding)
        
        # 컨텍스트 구성
        context = "\n".join([doc['_source']['content'] for doc in similar_docs])
        
        # LLM으로 응답 생성
        answer = await llm.generate(request.question, context)
        
        return QueryResponse(
            answer=answer,
            sources=[doc['_source']['source'] for doc in similar_docs]
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 