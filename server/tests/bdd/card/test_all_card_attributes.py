from pytest_bdd import parsers, scenarios, then, when
from table_parser.table_parser import table_parser  # type: ignore

from app.models.models import Cards
from tests.bdd.common_steps import *  # noqa
from tests.bdd.utils import fix

scenarios("all_card_attributes.feature")


@when(parsers.cfparse("creating a card with all attributes filled in\n{table}"))
def created_card_with_all_att(table, session):
    table = fix(table_parser(table))
    card = Cards()

    data = {}
    for row in table:
        data[row["attribute"]] = row["value"]

    card.number = data["num"]
    card.english_word = data["english word"]
    card.english_sentence = data["english sentence"]
    card.portuguese_word = data["portuguese word"]
    card.portuguese_sentence = data["portuguese sentence"]

    session.add(card)
    session.commit()


@then(parsers.cfparse("card 1 has the following attributes\n{table}"))
def has_the_following_attributes(table, session, client):
    table = fix(table_parser(table))
    data = {}
    for row in table:
        data[row["attribute"]] = row["value"]

    card = client.get("/cards/1").json

    assert card["number"] == int(data["num"])
    assert card["english_word"] == data["english word"]
    assert card["english_sentence"] == data["english sentence"]
    assert card["portuguese_word"] == data["portuguese word"]
    assert card["portuguese_sentence"] == data["portuguese sentence"]
