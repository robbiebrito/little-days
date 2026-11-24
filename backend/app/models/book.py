
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from app.db.database import Base


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)
    author = Column(String, nullable=True)
    total_pages = Column(Integer, nullable=True)

    current_page = Column(Integer, default=0)
    status = Column(String, default="want_to_read")

    created_at = Column(DateTime, default=datetime.utcnow)
