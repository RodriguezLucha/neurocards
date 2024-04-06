import factory
from factory import Sequence
from factory.alchemy import SQLAlchemyModelFactory

from app.models.models import Cards, Piles, State, db


class CardsFactory(SQLAlchemyModelFactory):
    class Meta:
        sqlalchemy_session = db.session
        model = Cards

    number = Sequence(lambda n: n)
    english_word = factory.Faker("word")  # type: ignore
    english_sentence = ""
    portuguese_word = factory.Faker("word")  # type: ignore
    portuguese_sentence = ""


class PilesFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Piles
        sqlalchemy_session = db.session

    pile_name = Sequence(lambda n: "pile_{}".format(n))


class StateFactory(SQLAlchemyModelFactory):
    class Meta:
        model = State
        sqlalchemy_session = db.session

    index = Sequence(lambda n: n)
    card_order = None
    chosen_pile_name = "name"
