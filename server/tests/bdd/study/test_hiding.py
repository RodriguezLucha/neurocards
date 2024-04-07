from pytest_bdd import scenarios, when

from tests.bdd.common_steps import *  # noqa

scenarios("hiding.feature")


@when("hiding the current card")
def hiding_the_current_card(client):
    res = client.get("/hide")
    assert res.status_code == 200
