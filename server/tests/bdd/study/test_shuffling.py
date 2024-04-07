from pytest_bdd import scenarios, when

from tests.bdd.common_steps import *  # noqa

scenarios("shuffling.feature")


@when("shuffling the pile with the reverse strategy")
def shuffling_the_pile_with_reverse(client, mocker):

    def reverse_array(arr):
        return arr[::-1]

    mocker.patch("api.routes.iteration.my_shuffle", side_effect=reverse_array)

    res = client.get("/shuffle")
    assert res.status_code == 200


@when("resetting the order")
def resetting_the_order(client):
    res = client.get("/reset")
    assert res.status_code == 200
