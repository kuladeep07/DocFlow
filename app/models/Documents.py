from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from app.db.base import Base


class Documents(Base):
    __tablename__ = "documents"

    ID: Mapped[int] = MappedColumn(Integer, primary_key=True)
    documentName: Mapped[str] = MappedColumn(String(100), nullable=False)
    userID: Mapped[int] = MappedColumn(ForeignKey("user_account.id"))
