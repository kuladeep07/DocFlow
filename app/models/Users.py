from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, MappedColumn

from app.db.base import Base


class Users(Base):
    __tablename__ = "user_account"

    id: Mapped[int] = MappedColumn(Integer, primary_key=True)
    username: Mapped[str] = MappedColumn(String(50), nullable=False)
    hashedpassword: Mapped[str] = MappedColumn(String(100), nullable=False)