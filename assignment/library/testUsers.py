# 653380120-2 กัมแพงเพชร สิงห์ขรณ์ Section 1

import pytest
from main import User


def test_create_user(db_session):
    #add
    new_user = User(username='_jhon2T', fullname='Jhon Uchiha', has_book=True)
    db_session.add(new_user)
    db_session.commit()

    # Query the _jhon2T to see if it is there
    user = db_session.query(User).filter_by(username='_jhon2T').first()
    assert user.username == "_jhon2T"
    assert user.fullname == "Jhon Uchiha"
    assert user.has_book is True


def test_delete_user(db_session):
    #add
    user = User(username='_jhon1T', fullname='Jhon Satoru', has_book=True)
    db_session.add(user)
    db_session.commit()

    #delete
    db_session.delete(user)
    db_session.commit()

    # Query the _jhon1T to check if it is removed from the db
    user = db_session.query(User).filter_by(username='_jhon1T').first()
    assert user is None
