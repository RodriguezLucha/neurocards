from pytest_bdd import given, parsers, scenarios, then, when

from api.models.models import State
from tests.bdd.common_steps import *  # noqa

scenarios("shuffling.feature")


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


@when("shuffling the pile with the reverse strategy")
def shuffling_the_pile_with_reverse(client, mocker):

    def reverse_array(arr):
        return arr[::-1]

    mocker.patch("api.routes.iteration.my_shuffle", side_effect=reverse_array)

    res = client.get("/shuffle")
    assert res.status_code == 200


@then(parsers.parse("the card number is {card_num:d}"))
def the_card_num_is(request, card_num):
    assert request.data["number"] == card_num


@then(parsers.parse("the card order will be [{card_order}]"))
def the_card_order_will_be(request, card_order):
    order = convert_order(card_order)
    assert request.data["card_order"] == order


@when("resetting the order")
def resetting_the_order(client):
    res = client.get("/reset")
    assert res.status_code == 200
