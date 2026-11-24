
from sqlalchemy.orm import Session

from app.models.book import Book
from app.schemas.book import BookCreate, BookUpdate


def create_book(db: Session, book: BookCreate):
    new_book = Book(
        title=book.title,
        author=book.author,
        total_pages=book.total_pages
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return new_book


def get_books(db: Session):
    return db.query(Book).all()


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def delete_book(db: Session, book_id: int):
    book = get_book(db, book_id)

    if book is None:
        return None

    db.delete(book)
    db.commit()

    return book

def update_book(db: Session, book_id: int, book_data: BookUpdate):
    book = get_book(db, book_id)

    if book is None:
        return None

    update_data = book_data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(book, field, value)

    db.commit()
    db.refresh(book)

    return book