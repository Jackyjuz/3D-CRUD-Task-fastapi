from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError

from .models import Base, Book
from .schemas import BookCreate, BookUpdate
from .crud import get_books, create_book, get_book, update_book, delete_book

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the database tables
Base.metadata.create_all(bind=engine)

@app.post("/books/", response_model=BookCreate)
def add_book(book: BookCreate):
    db = SessionLocal()
    try:
        return create_book(db=db, book=book)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Book already exists.")
    finally:
        db.close()

@app.get("/books/")
def get_all_books():
    db = SessionLocal()
    try:
        return get_books(db)
    finally:
        db.close()

@app.get("/books/{book_id}")
def get_book_by_id(book_id: int):
    db = SessionLocal()
    try:
        return get_book(db, book_id)
    except HTTPException:
        db.close()
        raise

@app.put("/books/{book_id}")
def update_book_details(book_id: int, book: BookUpdate):
    db = SessionLocal()
    try:
        return update_book(db, book_id, book)
    except HTTPException:
        db.close()
        raise

@app.delete("/books/{book_id}")
def remove_book(book_id: int):
    db = SessionLocal()
    try:
        return delete_book(db, book_id)
    except HTTPException:
        db.close()
        raise
