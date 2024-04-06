from pytest_bdd import given


def fix(data):
    return [dict(zip(data.keys(), values)) for values in zip(*data.values())]


@given("no cards are created")
def no_cards_are_created(clear):
    # called clear already here
    pass
