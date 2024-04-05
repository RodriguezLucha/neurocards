from pytest_bdd import given, parsers, scenarios, then, when
from table_parser.table_parser import table_parser

scenarios("card_management.feature")


def fix_table(data):
    return [dict(zip(data.keys(), values)) for values in zip(*data.values())]


@given("no cards are created")
def no_cards_are_created(clear):
    pass


@when(parsers.cfparse("creating cards\n{table}"))
def creating_cards(table, cards_factory, session):
    table_dict = table_parser(table)
    table = fix_table(table_dict)
    for row in table:
        card = cards_factory.create(
            number=row["num"],
            english_word=row["english word"],
            portuguese_word=row["portuguese word"],
        )
        session.add(card)
        session.commit()


@then(parsers.parse("{:d} card is created"))
def card_is_created():
    pass


@given(parsers.cfparse("the following existing cards\n{table}"))
def the_following_existing_cards(table):
    pass


@when(parsers.cfparse("updating card {card_num} with values\n{table}"))
def updating_card_with_values():
    pass


@then(parsers.cfparse("the following cards exist\n{table}"))
def the_following_cards_exist():
    pass


@when(parsers.parse("deleting card {card_num}"))
def deleting_card():
    pass
