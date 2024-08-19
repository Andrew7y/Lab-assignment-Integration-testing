# 653380120-2 กัมแพงเพชร สิงห์ขรณ์ Section 1

import pytest
from main import Book


def test_create_Book(db_session):
    #add
    newBook = Book(title="Harry Potter", firstauthor="Satoru GoJo", isbn="1221334")
    db_session.add(newBook)
    db_session.commit()

    # Query the Harry Potter to see if it is there
    book = db_session.query(Book).filter_by(title="Harry Potter", firstauthor="Satoru GoJo", isbn="1221334").first()
    assert book.title == "Harry Potter"
    assert book.isbn == "1221334"
    assert book.firstauthor == "Satoru GoJo"


def test_delete_book(db_session):
    #add
    book = Book(title="Harry Potter2", firstauthor="Satoru GoJo", isbn="1221335")
    db_session.add(book)
    db_session.commit()

    #delete
    db_session.delete(book)
    db_session.commit()

    # Query the Harry Potter2 to check if it is removed from the db
    user = db_session.query(Book).filter_by(title="Harry Potter2", firstauthor="Satoru GoJo", isbn="1221335").first()
    assert user is None

