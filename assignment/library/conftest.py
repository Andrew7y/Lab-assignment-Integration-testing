# 653380120-2 กัมแพงเพชร สิงห์ขรณ์ Section 1

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Base

DatabaseURL = "sqlite:///./library.db"


@pytest.fixture(scope="session")
def engine():
    engine = create_engine(DatabaseURL, connect_args={"check_same_thread": False})
    return engine


@pytest.fixture(scope="session")
def setup_database(engine):
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="session")
def db_session(engine, setup_database):
    connection = engine.connect()
    transaction = connection.begin()
    session = sessionmaker(bind=connection)()

    yield session

    session.close()
    transaction.rollback()
    connection.close()

