import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app import crud, schemas

# In-memory SQLite for tests
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(bind=engine)

@pytest.fixture(scope="module")
def db():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_create_and_get_book(db):
    book_in = schemas.BookCreate(
        title="Test", author="Author", published_year=2020, summary="Desc"
    )
    book = crud.create_book(db, book_in)
    assert book.id == 1
    fetched = crud.get_book(db, book.id)
    assert fetched.title == "Test"

def test_update_book(db):
    update_in = schemas.BookUpdate(title="Updated")
    updated = crud.update_book(db, 1, update_in)
    assert updated.title == "Updated"

def test_delete_book(db):
    deleted = crud.delete_book(db, 1)
    assert deleted.id == 1
    assert crud.get_book(db, 1) is None