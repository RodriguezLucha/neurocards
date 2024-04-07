from pytest_bdd import given, parsers, scenarios, then, when

from api.models.models import State
from tests.bdd.common_steps import *  # noqa

scenarios("flipping.feature")


@given("is facing the front")
def is_facing_the_front(session):
    state: State = session.query(State).first()  # type: ignore
    assert state.show_front is True


@given("is facing the back")
def is_facing_the_back(session):
    state: State = session.query(State).first()  # type: ignore
    state.show_front = False
    session.add(state)
    session.commit()


@when("flipping the card")
def flipping_the_card(client):
    res = client.get("/flip")
    assert res.status_code == 200


@then(parsers.parse("the word is {word}"))
def the_word_is(request, word):
    assert request.data["word"] == word
