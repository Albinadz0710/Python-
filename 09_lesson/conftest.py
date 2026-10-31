import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = DATABASE_URL = "postgresql+psycopg2://myuser:mypassword@localhost:5432/mydatabase"

@pytest.fixture(scope="session")
def engine():
    eng = create_engine(DATABASE_URL, future=True)
    yield eng
    eng.dispose()

@pytest.fixture()
def session(engine):
    with engine.connect() as connection:
        trans = connection.begin()
        Session = sessionmaker(bind=connection, future=True)
        sess = Session()
        try:
            yield sess
        finally:
            sess.close()
            trans.rollback()

