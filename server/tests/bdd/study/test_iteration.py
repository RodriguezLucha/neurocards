from pprint import pprint

from pytest_bdd import given, parsers, scenarios, then, when
from table_parser.table_parser import table_parser  # type: ignore

from api.models.factories import CardsFactory, StateFactory
from api.models.models import Piles, State
from tests.bdd.utils import fix

scenarios("iteration.feature")


# @given("no cards are created")
# def no_cards_are_created(clear):
#     # called clear already here
#     pass


@given(parsers.cfparse("the following card database\n{table}"))
def the_following_card_database(clear, session, table):
    # parse the table
    table = fix(table_parser(table))

    # iterate the rows
    for row in table:
        # create the pile if it doesn't exist
        count = session.query(Piles).where(Piles.pile_name == row["pile"]).count()
        if count < 1:
            pile = Piles()
            pile.pile_name = row["pile"]
            session.add(pile)
            session.commit()

        # create the cards
        card = CardsFactory.create(
            number=row["num"],
            english_word=row["english word"],
            portuguese_word=row["portuguese word"],
            pile_name=row["pile"],
        )
        session.add(card)

    # commit
    session.commit()


@given(parsers.parse("the selected pile is {pile}"))
def the_seleted_pile_is(pile, session):
    create_state_if_does_not_exist(session)
    state: State = session.query(State).first()  # type: ignore
    state.chosen_pile_name = pile
    pprint(state.to_dict())
    session.add(state)
    session.commit()


def create_state_if_does_not_exist(session):
    count = session.query(State).count()
    if count < 1:
        state = StateFactory()
        session.add(state)
        session.commit()


@when("going to the next card")
def going_to_the_next_card():
    pass


@then(parsers.parse("the selected card will be {selected}"))
def the_selected_card_will_be(selected):
    pass
