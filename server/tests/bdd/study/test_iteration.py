from pytest_bdd import given, parsers, scenarios, then, when

from api.models.factories import StateFactory
from api.models.models import Cards, State
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


@then(parsers.parse("the selected card will be {selected:d}"))
def the_selected_card_will_be(selected, client):
    res = client.get("/current")
    data = res.json
    assert res.status_code == 200
    current_card_number = data["number"]
    assert current_card_number == selected
