import factory
import pytest
from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models.models import Base, Cards, Piles, State
from tests.drivers.ui import UIDriver

global_session = None


def pytest_addoption(parser):
    parser.addoption("--driver", action="store")


@pytest.fixture
def app_driver(request):
    selected = request.config.getoption("--driver")
    driver = None
    if selected == "ui":
        driver = UIDriver()
    else:
        raise Exception("Unknown driver. Available: ui")
    yield driver


@pytest.fixture(scope="session")
def engine():
    url = "postgresql://postgres:password@localhost/neurocards"
    engine = create_engine(url)
    Base.metadata.create_all(engine)
    yield engine


@pytest.fixture(scope="session", autouse=True)
def session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    global global_session
    global_session = session
    yield session
    session.close()


@pytest.fixture()
def clear(session):
    session.query(Cards).delete()


@pytest.fixture
def cards_factory(session):

    class CardsFactory(SQLAlchemyModelFactory):
        class Meta:
            model = Cards
            sqlalchemy_session = session

        number = Sequence(lambda n: n)
        english_word = factory.Faker("word")
        english_sentence = factory.Faker("sentence")
        portuguese_word = factory.Faker("word")
        portuguese_sentence = factory.Faker("sentence")

    yield CardsFactory


class PilesFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Piles
        sqlalchemy_session = global_session

    pile_name = Sequence(lambda n: "pile_{}".format(n))


class StateFactory(SQLAlchemyModelFactory):
    class Meta:
        model = State
        sqlalchemy_session = global_session

    index = Sequence(lambda n: n)
    card_order = None
    chosen_pile_name = "name"
