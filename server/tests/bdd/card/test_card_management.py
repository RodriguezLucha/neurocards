from pytest_bdd import given, parsers, scenarios, then, when
from sqlalchemy import delete
from table_parser.table_parser import table_parser  # type: ignore

from models.models import Cards
from tests.bdd.common_steps import *  # noqa
from tests.bdd.utils import fix

scenarios("card_management.feature")


@when(parsers.cfparse("creating cards\n{table}"))
def creating_cards(table, cards_factory, session):
    table = fix(table_parser(table))
    for row in table:
        card = cards_factory.create(
            number=row["num"],
            english_word=row["english word"],
            portuguese_word=row["portuguese word"],
        )
        session.add(card)
        session.commit()


@then(parsers.parse("{num_cards:d} cards are created"))
def card_is_created(num_cards, session):
    num_rows = session.query(Cards).count()
    assert num_rows == num_cards


@given(parsers.cfparse("the following existing cards\n{table}"))
def the_following_existing_cards(clear, table, cards_factory, session):
    table = fix(table_parser(table))
    for row in table:
        card = cards_factory.create(
            number=row["num"],
            english_word=row["english word"],
            portuguese_word=row["portuguese word"],
        )
        session.add(card)
        session.commit()


@when(parsers.cfparse("updating card {card_num} with values\n{table}"))
def updating_card_with_values(card_num, table, session):
    card = session.query(Cards).where(Cards.number == card_num).first()
    table = table_parser(table)
    card.english_word = table["english word"][0]
    card.portuguese_word = table["portuguese word"][0]
    session.add(card)
    session.commit()


@then(parsers.cfparse("the following cards exist\n{table}"))
def the_following_cards_exist(table, session):
    table = fix(table_parser(table))
    cards = session.query(Cards).all()
    for row, card in zip(table, cards):
        assert int(row["num"]) == card.number
        assert row["english word"] == card.english_word
        assert row["portuguese word"] == card.portuguese_word


@when(parsers.parse("deleting card {card_num}"))
def deleting_card(card_num, session):
    stmt = delete(Cards).where(Cards.number.in_([card_num]))
    session.execute(stmt)
