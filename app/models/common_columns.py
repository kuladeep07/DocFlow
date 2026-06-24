from datetime import datetime

from sqlalchemy import INTEGER, DATETIME, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class CommonColumns(Base):
    created_by: Mapped[int] = mapped_column(INTEGER, ForeignKey("user_account.user_id"), nullable=False)
    created_date: Mapped[datetime] = mapped_column(DATETIME, nullable=False)
    updated_by: Mapped[int] = mapped_column(INTEGER, nullable=False)
    updated_date: Mapped[datetime] = mapped_column(DATETIME, ForeignKey("user_account.user_id"), nullable=False)

