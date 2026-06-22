from fastapi import APIRouter

documents_router = APIRouter()

@documents_router.post("/documents")
def upload_documents():
    ### POST /v1/documents → Uploads to MinIO/S3, enqueues Celery job, returns job_id
    ...

@documents_router.get("/documents/{job_id}/status")
def get_document_status(job_id):
    ### ─ GET  /v1/documents/{job_id}/status → Polls Celery result backend (Redis)
    ...


@documents_router.get("/documents/{job_id}/result")
def get_document_results(job_id):
    ###  Returns cached result from Redis or PostgreSQL
    ...

