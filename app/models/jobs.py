from datetime import datetime

from sqlalchemy import ForeignKey, String, Integer, DATETIME
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base
from app.models.common_columns import CommonColumns


class Jobs(Base, CommonColumns):
    __tablename__ = "jobs"

    job_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    document_id: Mapped[int] = mapped_column(Integer, ForeignKey("documents.document_id"))
    job_status: Mapped[str] = mapped_column(String(10),nullable=False)
    start_time: Mapped[datetime] = mapped_column(DATETIME , nullable=False)
    end_time: Mapped[datetime] = mapped_column(DATETIME , nullable=False)
    error_message: Mapped[str] = mapped_column(String(100),nullable=True)
    celery_task_id: Mapped[str] = mapped_column(String(50), nullable=False)
    retry_count: Mapped[int] = mapped_column(Integer, nullable=False)
    results: Mapped[str] = mapped_column(String(100), nullable=True)



