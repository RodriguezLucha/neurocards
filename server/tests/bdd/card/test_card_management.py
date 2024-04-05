from pytest_bdd import given, parsers, scenarios, then, when
from table_parser.table_parser import table_parser

scenarios("card_management.feature")


@given("no cards are created")
def no_cards_are_created():
    pass


@when(parsers.cfparse("creating cards\n{table}"))
def creating_cards(table):
    table_dict = table_parser(table)
    print(table_dict)


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
