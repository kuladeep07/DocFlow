from fastapi import UploadFile
from sqlalchemy.orm import Session


def process_documents(file: UploadFile):
    return {"status": "completed"}