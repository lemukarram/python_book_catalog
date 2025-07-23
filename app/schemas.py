from pydantic import BaseModel, Field, ConfigDict

class BookBase(BaseModel):
    title: str
    author: str
    published_year: int
    summary: str

class BookCreate(BookBase):
    pass

class BookUpdate(BaseModel):
    title: str | None = None
    author: str | None = None
    published_year: int | None = Field(None, ge=0, le=2100)
    summary: str | None = None

class Book(BookBase):
    id: int
    title: str
    author: str
    published_year: int
    summary: str | None = None

    model_config = ConfigDict(from_attributes=True)