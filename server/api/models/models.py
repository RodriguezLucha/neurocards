from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ARRAY, Boolean, Column, ForeignKey, Integer, Text
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy_serializer import SerializerMixin  # type: ignore


class Base(DeclarativeBase):
    pass


class Cards(Base, SerializerMixin):
    __tablename__ = "Cards"
    number = Column(Integer, primary_key=True)
    english_word = Column(Text)
    english_sentence = Column(Text)
    portuguese_word = Column(Text)
    portuguese_sentence = Column(Text)
    pile_name = Column(Text, ForeignKey("Piles.pile_name"))
    hidden = Column(Boolean, default=False)


class Piles(Base, SerializerMixin):
    __tablename__ = "Piles"
    pile_name = Column(Text, primary_key=True)


class State(Base, SerializerMixin):
    __tablename__ = "State"
    index = Column(Integer, primary_key=True)
    card_order = Column(MutableList.as_mutable(ARRAY(Integer)))
    chosen_pile_name = Column(Text, ForeignKey("Piles.pile_name"))
    chosen_pile = relationship("Piles")
    show_front = Column(Boolean, default=True)


db = SQLAlchemy(model_class=Base)
