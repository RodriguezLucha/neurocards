from pytest_bdd import given, parsers, then, when
from table_parser.table_parser import table_parser  # type: ignore

from api.models.factories import CardsFactory, StateFactory
from api.models.models import Cards, Piles, State
from tests.bdd.utils import fix


@given("no cards are created")
def no_cards_are_created(clear):
    # called clear already here
    pass


@given(parsers.cfparse("the following card database\n{table}"))
def the_following_card_database(clear, session, table):
    table = fix(table_parser(table))

    for row in table:
        count = session.query(Piles).where(Piles.pile_name == row["pile"]).count()
        if count < 1:
            pile = Piles()
            pile.pile_name = row["pile"]
            session.add(pile)
            session.commit()

        card = CardsFactory.create(
            number=row["num"],
            english_word=row["english word"],
            portuguese_word=row["portuguese word"],
            pile_name=row["pile"],
        )
        session.add(card)

    session.commit()


def create_state_if_does_not_exist(session):
    count = session.query(State).count()
    if count < 1:
        state = StateFactory()
        session.add(state)
        session.commit()


@given(parsers.parse("the selected pile is {pile}"))
def the_seleted_pile_is(pile, session):
    create_state_if_does_not_exist(session)
    state: State = session.query(State).first()  # type: ignore
    state.chosen_pile_name = pile

    cards = session.query(Cards).where(Cards.pile_name == pile).all()
    card_nums = [c.number for c in cards]
    state.card_order = card_nums
    state.index = 0
    session.add(state)
    session.commit()


@given(parsers.parse("the selected card is {card_num:d}"))
def the_selected_card_is(card_num, session):
    state: State = session.query(State).first()  # type: ignore
    pile_name = state.chosen_pile_name
    cards = session.query(Cards).where(Cards.pile_name == pile_name).all()

    for i, card in zip(list(range(len(cards))), cards):
        if card.number == card_num:
            state.index = i
            session.add(state)
            session.commit()


@when("viewing the card")
def viewing_the_card(request, client):
    res = client.get("/current")
    assert res.status_code == 200
    data = res.json
    request.data = data


@then(parsers.parse("the selected card will be {selected:d}"))
def the_selected_card_will_be(selected, client):
    res = client.get("/current")
    data = res.json
    assert res.status_code == 200
    current_card_number = data["number"]
    assert current_card_number == selected


def convert_order(card_order):
    order = card_order.split(",")
    order = [int(x) for x in order]
    return order


@given(parsers.parse("the card order is [{card_order}]"))
def the_card_order_is(session, card_order):
    order = convert_order(card_order)
    state = session.query(State).first()
    state.card_order = order
    session.add(state)
    session.commit()


@then(parsers.parse("the card order will be [{card_order}]"))
def the_card_order_will_be(request, card_order):
    order = convert_order(card_order)
    assert request.data["card_order"] == order
