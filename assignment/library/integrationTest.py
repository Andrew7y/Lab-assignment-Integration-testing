# 653380120-2 กัมแพงเพชร สิงห์ขรณ์ Section 1

import pytest
from fastapi.testclient import TestClient
from main import User, Book, get_db, app, Borrowlist


@pytest.fixture
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    return TestClient(app)


def test_borrow_books(client, db_session):
    user = User(username="01_itxchi", fullname="Itachi Uchiha", has_book=True)
    db_session.add(user)
    db_session.commit()

    book = Book(title="Introduction to Python Programming", firstauthor="John Doe", isbn="978-1234567890")
    db_session.add(book)
    db_session.commit()

    response = client.post(f"/borrowlist/?user_id={user.id}&book_id={book.id}")
    assert response.json()["user_id"] == user.id
    assert response.status_code == 200
    assert response.json()["book_id"] == book.id
    assert db_session.query(Borrowlist).filter_by(user_id=user.id, book_id=book.id).first()


def test_getBorrow_books(client, db_session):
    user = User(username="02_gojox", fullname="Satoru Gojo", has_book=True)
    db_session.add(user)
    db_session.commit()

    book = Book(title="Introduction to Python Programming", firstauthor="John Doe", isbn="978-1234567890")
    db_session.add(book)
    db_session.commit()

    borrowlist = Borrowlist(user_id=user.id, book_id=book.id)
    db_session.add(borrowlist)
    db_session.commit()

    response = client.get(f"/borrowlist/{user.id}")
    assert response.status_code == 200
    assert db_session.query(Borrowlist).filter_by(user_id=user.id).all()
    assert response.json()[0]["book_id"] == book.id
    assert response.json()[0]["user_id"] == user.id
