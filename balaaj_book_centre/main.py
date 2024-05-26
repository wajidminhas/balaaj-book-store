from fastapi import FastAPI, Depends, HTTPException
from balaaj_book_centre.book_db import get_session, create_db     
from contextlib import asynccontextmanager
from balaaj_book_centre.book_db import Book
from typing import Annotated
from sqlmodel import Session


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("creating table")
    create_db()
    yield
    print("table created")


app : FastAPI = FastAPI(lifespan=lifespan)    

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/create_book")
async def create_book(book: Book, session: Annotated[Session, Depends(get_session)]):
    session.add(book)
    session.commit()
    session.refresh(book)
    return {"Book" : book}

@app.get("/get_books")
async def get_books(session: Annotated[Session, Depends(get_session)]):
    try:
        books = session.query(Book).all()
        return {"books": books}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# TO GET SINGLE BOOK 
    
@app.get("/get_book/{id}")
async def get_single_book(id: int, session: Annotated[Session, Depends(get_session)]):
    try:
        book = session.query(Book).filter(Book.id == id).first()
        return {"book": book}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# TO UPDATE BOOK 

@app.put("/update_book/{id}")
async def update_book(id: int, book: Book, session: Annotated[Session, Depends(get_session)]):
    try:
        book = session.query(Book).filter(Book.id == id).first()
        book.title = book.title
        session.commit()
        return {"message": "Book updated"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
# TO DELETE BOOK FROM DB 
    
@app.delete("/delete_book/{id}")
async def remove_book(id: int, session: Annotated[Session, Depends(get_session)]):
    try:
        book = session.query(Book).filter(Book.id == id).first()
        session.delete(book)
        session.commit()
        return {"message": "Book deleted"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))




