from pydantic import BaseModel, Field

class BookBase(BaseModel):
    title: str = Field(..., example="The Odyssey")
    author: str = Field(..., example="Homer")
    published_year: int = Field(..., ge=0, le=2100, example=800)
    summary: str | None = Field(None, example="An epic poem...")

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    published_year: int | None = Field(None, ge=0, le=2100)
    summary: str | None = None

class Book(BookBase):
    id: int

    class Config:
        orm_mode = True