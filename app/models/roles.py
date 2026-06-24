

from sqlalchemy import INTEGER, String
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Roles(Base):
    __tablename__ = "roles"

    role_id: Mapped[int] = mapped_column(INTEGER, nullable=False)
    role_name: Mapped[str] = mapped_column(String(50), nullable=False)
