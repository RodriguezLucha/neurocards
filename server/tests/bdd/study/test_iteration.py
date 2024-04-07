from pytest_bdd import scenarios, when

from tests.bdd.common_steps import *  # noqa

scenarios("iteration.feature")


@when("going to the next card")
def going_to_the_next_card(client):
    res = client.get("/next")
    assert res.status_code == 200


@when("going to the previous card")
def going_to_the_previous_card(client):
    res = client.get("/previous")
    assert res.status_code == 200
