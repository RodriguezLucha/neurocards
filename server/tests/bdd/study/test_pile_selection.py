from pytest_bdd import given, parsers, scenarios, when

from tests.bdd.common_steps import *  # noqa

scenarios("pile_selection.feature")


@given("no pile is selected")
def no_pile_is_selected(session):
    create_state_if_does_not_exist(session)  # noqa


@when(parsers.parse("selecting pile {pile}"))
def the_selected_pile_is(pile, client):
    res = client.get(f"/switch/{pile}")
    assert res.status_code == 200
