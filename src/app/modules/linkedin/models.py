from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, DateTime
from sqlalchemy.sql import func

from src.app.core.db import Base

class ProfileUrl(Base):
    __tablename__ = "profile_url"
    __table_args__ = {"schema": "linkedin"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(String(100), unique=True)
    
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    deleted_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True, default=None)
    
    def __repr__(self) -> str:
        return f"ProfileUrl(id={self.id!r}, url={self.url!r})"


class PageUrl(Base):
    __tablename__ = "page_url"
    __table_args__ = {"schema": "linkedin"}
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    url: Mapped[str] = mapped_column(String(100), unique=True)
    
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)
    deleted_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), nullable=True, default=None)
    
    def __repr__(self) -> str:
        return f"PageUrl(id={self.id!r}, url={self.url!r})"
