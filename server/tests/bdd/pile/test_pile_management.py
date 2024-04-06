from pytest_bdd import given, scenarios

scenarios("pile_management.feature")


@given("no piles are created")
def no_cards_are_created(clear):
    # called clear already here
    pass
