from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, relationship, mapped_column

from app.db.base import Base
from app.models.common_columns import CommonColumns


class Documents(Base, CommonColumns):
    __tablename__ = "documents"

    document_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    documentName: Mapped[str] = mapped_column(String(100), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.user_id"), nullable=False)
    filepath: Mapped[str] = mapped_column(String(100), nullable=False)
    file_size: Mapped[str] = mapped_column(String(50), nullable=False)
    mime_type: Mapped[str] = mapped_column(String(50), nullable=False)
    upload_status: Mapped[str] = mapped_column(String(50), nullable=False)
