
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.book import BookCreate, BookResponse, BookUpdate
from app.services import book_service

router = APIRouter(
    prefix="/books",
    tags=["Reading"]
)


@router.post("/", response_model=BookResponse)
def create_book(
    book: BookCreate,
    db: Session = Depends(get_db)
):
    return book_service.create_book(db, book)


@router.get("/", response_model=List[BookResponse])
def get_books(db: Session = Depends(get_db)):
    return book_service.get_books(db)


@router.get("/{book_id}", response_model=BookResponse)
def get_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    book = book_service.get_book(db, book_id)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book


@router.delete("/{book_id}")
def delete_book(
    book_id: int,
    db: Session = Depends(get_db)
):
    book = book_service.delete_book(db, book_id)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return {"message": "Book deleted successfully"}

@router.patch("/{book_id}", response_model=BookResponse)
def update_book(
    book_id: int,
    book_data: BookUpdate,
    db: Session = Depends(get_db)
):
    book = book_service.update_book(db, book_id, book_data)

    if book is None:
        raise HTTPException(
            status_code=404,
            detail="Book not found"
        )

    return book
