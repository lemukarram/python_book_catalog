Book Catalog API

Overview

This repository contains a simple Book Catalog CRUD service built with FastAPI, SQLAlchemy, Pydantic, and SQLite. It demonstrates database models, Pydantic schemas, asynchronous endpoints, and a comprehensive test suite.

Features

List all books

Retrieve a book by ID

Create a new book

Update an existing book

Delete a book

Automatic OpenAPI documentation (Swagger UI & ReDoc)

Tech Stack

Python 3.8+

FastAPI

SQLAlchemy (SQLite)

Pydantic

Uvicorn

Pytest

Getting Started

Prerequisites

Git installed

Python 3.8 or newer

Optional: Docker (for containerized deployment)

Installation

Clone the repository

git clone https://github.com/lemukarram/python_book_catalog.git
cd python_book_catalog

Create and activate a virtual environment

python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

Install dependencies

pip install -r requirements.txt

Project Structure

book_catalog/
├── app/
│   ├── __init__.py
│   ├── database.py       # SQLAlchemy setup
│   ├── models.py         # ORM models
│   ├── schemas.py        # Pydantic schemas
│   ├── crud.py           # CRUD logic
│   └── main.py           # FastAPI application
├── tests/
│   ├── __init__.py
│   ├── test_crud.py      # Unit tests for CRUD logic
│   └── test_main.py      # Integration tests for API endpoints
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

Running the Application

Start the FastAPI server with automatic reload:

uvicorn app.main:app --reload

Open your browser and navigate to:

Swagger UI: http://127.0.0.1:8000/docs

ReDoc:      http://127.0.0.1:8000/redoc

API Endpoints

Method

Path

Description

GET

/books/

List all books

GET

/books/{id}

Retrieve a book by ID

POST

/books/

Create a new book

PUT

/books/{id}

Update an existing book

DELETE

/books/{id}

Delete a book

Example: create a new book via curl

curl -X POST "http://127.0.0.1:8000/books/" \
     -H "Content-Type: application/json" \
     -d '{
       "title":"1984",
       "author":"George Orwell",
       "published_year":1949,
       "summary":"Dystopian novel."
     }'

Testing

Run the full test suite:

pytest -q

Docker (Optional)

Build and run a Docker container:

docker build -t book-catalog .
docker run -p 8000:80 book-catalog

The service will be available at http://localhost:8000.

Contributing

Contributions are welcome. Please fork the repository, create a feature branch, and open a pull request.

License

This project is released under the MIT License. See the LICENSE file for details.
