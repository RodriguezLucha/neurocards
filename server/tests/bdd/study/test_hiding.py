from pytest_bdd import parsers, scenarios, then, when
from table_parser.table_parser import table_parser  # type: ignore

from api.models.models import Cards
from tests.bdd.common_steps import *  # noqa
from tests.bdd.utils import fix

scenarios("hiding.feature")


@when("hiding the current card")
def hiding_the_current_card(client):
    res = client.get("/hide")
    assert res.status_code == 200


@then(parsers.cfparse("the card database has\n{table}"))
def the_card_database_has(clear, session, table):
    table = fix(table_parser(table))
    cards = session.query(Cards).order_by(Cards.number).all()
    for row, card in zip(table, cards):
        assert int(row["num"]) == card.number
        assert row["english word"] == card.english_word
        assert row["portuguese word"] == card.portuguese_word
        assert row["hidden"] == "yes" if card.hidden else "no"
