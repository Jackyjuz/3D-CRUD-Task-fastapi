from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    author: str
    published_year: int
    isbn: str

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    published_year: int | None = None
    isbn: str | None = None

    class Config:
        orm_mode = True
