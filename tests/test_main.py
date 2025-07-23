from fastapi.testclient import TestClient
from app.main import app
from app.database import Base, engine

client = TestClient(app)

def setup_module():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

def test_read_empty_books():
    response = client.get("/books/")
    assert response.status_code == 200
    assert response.json() == []

def test_crud_workflow():
    book = {"title": "Sample", "author": "Auth", "published_year": 2000, "summary": "Sum"}

    # Create
    r = client.post("/books/", json=book)
    assert r.status_code == 201
    created = r.json()
    book_id = created["id"]

    # Read single
    r = client.get(f"/books/{book_id}")
    assert r.status_code == 200

    # Update
    update = {**book, "title": "New Title"}
    r = client.put(f"/books/{book_id}", json=update)
    assert r.json()["title"] == "New Title"

    # Delete
    r = client.delete(f"/books/{book_id}")
    assert r.status_code == 200

    # Confirm deletion
    r = client.get(f"/books/{book_id}")
    assert r.status_code == 404