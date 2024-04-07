import pytest

from api.models.models import Cards, Piles, State, db
from app import app as myapp


@pytest.fixture(scope="session")
def app():
    return myapp


@pytest.fixture(scope="session", autouse=True)
def session(app):
    yield db.session


@pytest.fixture()
def clear(session):
    session.query(State).delete()
    session.query(Cards).delete()
    session.query(Piles).delete()
    session.commit()
