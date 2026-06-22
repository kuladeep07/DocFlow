from fastapi import APIRouter, UploadFile
from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.Documents import Documents
from app.services.documents.pipeline import process_documents

documents_router = APIRouter()

@documents_router.post("/documents")
def upload_documents(file: UploadFile,user_id: int, db:Session=Depends(get_db)):
    ### POST /v1/documents → Uploads to MinIO/S3, enqueues Celery job, returns job_id
    response = process_documents(file)
    document = Documents(documentName=file.filename, userID=user_id)
    db.add(document)
    db.commit()

    return response

@documents_router.get("/documents/{job_id}/status")
def get_document_status(job_id):
    ### ─ GET  /v1/documents/{job_id}/status → Polls Celery result backend (Redis)
    ...


@documents_router.get("/documents/{job_id}/result")
def get_document_results(job_id):
    ###  Returns cached result from Redis or PostgreSQL
    ...

