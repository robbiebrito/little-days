
from pydantic import BaseModel, ConfigDict
from typing import Optional


class BookCreate(BaseModel):
    title: str
    author: Optional[str] = None
    total_pages: Optional[int] = None

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    total_pages: Optional[int] = None

class BookResponse(BaseModel):
    id: int
    title: str
    author: Optional[str] = None
    total_pages: Optional[int] = None
    current_page: int
    status: str

    model_config = ConfigDict(from_attributes=True)
