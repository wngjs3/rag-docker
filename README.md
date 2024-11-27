# RAG API Service

RAG(Retrieval-Augmented Generation) API 서비스입니다. FastAPI와 OpenSearch를 활용하여 구현되었습니다.

## 시스템 요구사항

- Docker
- Docker Compose
- AWS 자격 증명 설정

## EC2 환경 설정

### Docker 설치
```bash
# 시스템 패키지 업데이트
sudo yum update -y

# Docker 설치
sudo yum install -y docker

# Docker 서비스 시작
sudo service docker start

# 현재 사용자를 docker 그룹에 추가 (로그아웃 후 다시 로그인 필요)
sudo usermod -a -G docker $USER

# Docker 서비스 자동 시작 설정
sudo systemctl enable docker
```

### Docker Compose 설치
```bash
# Docker Compose 설치
sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# 실행 권한 부여
sudo chmod +x /usr/local/bin/docker-compose

# 설치 확인
docker-compose --version
```

## 환경 설정

1. 개발 환경 설정 파일 생성
```
cp .env.dev.example .env.dev
```

2. `.env.dev` 파일에서 필요한 환경 변수 설정
```
DEBUG=True
AWS_REGION=ap-northeast-2
OPENSEARCH_ENDPOINT=your-opensearch-endpoint
INDEX_NAME=rag-embeddings
```

## 실행 스크립트

프로젝트 실행을 위한 편의성 스크립트들이 `scripts` 디렉토리에 준비되어 있습니다.
모든 스크립트는 환경(dev/prod)을 인자로 받을 수 있으며, 기본값은 `dev` 입니다.

### 서비스 빌드
```
# 개발 환경 빌드
./scripts/build.sh

# 프로덕션 환경 빌드
./scripts/build.sh prod
```

### 서비스 시작
```
# 개발 환경 시작
./scripts/start.sh

# 프로덕션 환경 시작
./scripts/start.sh prod
```

### 서비스 중지
```
# 개발 환경 중지
./scripts/stop.sh

# 프로덕션 환경 중지
./scripts/stop.sh prod
```

### 컨테이너 쉘 접속
```
# 개발 환경 컨테이너 쉘 접속
./scripts/shell.sh

# 프로덕션 환경 컨테이너 쉘 접속
./scripts/shell.sh prod
```

## 환경별 특징

### 개발 환경 (dev)
- 소스 코드 볼륨 마운트로 실시간 반영
- 디버그 모드 활성화
- Hot-reload 지원

### 프로덕션 환경 (prod)
- 컨테이너 내부에 소스 코드 복사
- 2개의 API 서버 레플리카 실행
- 헬스체크 설정
- 최적화된 실행 환경

## API 엔드포인트

- 헬스체크: `GET /health`
- API 문서: `GET /docs`

## 디렉토리 구조
```
.
├── src/                    # 소스 코드
│   ├── api/               # API 라우터 및 핸들러
│   ├── db/                # 데이터베이스 관련 코드
│   └── main.py           # 애플리케이션 엔트리포인트
├── scripts/               # 실행 스크립트
├── Dockerfile.dev         # 개발 환경 도커 설정
├── Dockerfile.prod        # 프로덕션 환경 도커 설정
├── docker-compose.dev.yml # 개발 환경 컴포즈 설정
└── docker-compose.prod.yml # 프로덕션 환경 컴포즈 설정
```

## AWS 설정

AWS 서비스를 사용하기 위해서는 적절한 IAM 권한이 필요합니다. 
다음 서비스에 대한 접근 권한이 필요합니다:

- OpenSearch Service
- EC2 (메타데이터 접근용)

로컬 개발 환경에서는 AWS CLI 설정이 필요합니다:
```
aws configure
```

## 문제 해결

### 일반적인 문제 해결 방법

1. 컨테이너 로그 확인
```
docker-compose -f docker-compose.dev.yml logs -f api
```

2. 컨테이너 재시작
```
./scripts/stop.sh && ./scripts/start.sh
```

3. 이미지 재빌드
```
./scripts/build.sh
```

### 알려진 이슈

- OpenSearch 연결 실패 시 환경 변수와 AWS 자격 증명을 확인하세요.
- Hot-reload가 작동하지 않을 경우 볼륨 마운트를 확인하세요.