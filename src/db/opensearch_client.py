from opensearchpy import OpenSearch, RequestsHttpConnection
from aws_requests_auth.aws_auth import AWSRequestsAuth
import boto3
from src.config import settings

class OpenSearchClient:
    def __init__(self):
        self.client = self._initialize_client()
        
    def _initialize_client(self) -> OpenSearch:
        """OpenSearch 클라이언트 초기화"""
        credentials = boto3.Session().get_credentials()
        auth = AWSRequestsAuth(
            aws_access_key=credentials.access_key,
            aws_secret_access_key=credentials.secret_key,
            aws_token=credentials.token,
            aws_host=settings.OPENSEARCH_ENDPOINT,
            aws_region=settings.AWS_REGION,
            aws_service='es'
        )
        
        return OpenSearch(
            hosts=[{'host': settings.OPENSEARCH_ENDPOINT, 'port': 443}],
            http_auth=auth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
        )
    
    async def search_similar(self, vector: List[float], k: int = 3) -> List[Dict]:
        """벡터 유사도 검색"""
        query = {
            "size": k,
            "query": {
                "knn": {
                    "embedding_vector": {
                        "vector": vector,
                        "k": k
                    }
                }
            }
        }
        
        response = self.client.search(
            body=query,
            index=settings.INDEX_NAME
        )
        
        return response['hits']['hits'] 