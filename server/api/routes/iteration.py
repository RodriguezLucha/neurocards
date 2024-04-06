from api.models.models import Cards, State, db


def next():
    session = db.session
    state = session.query(State).first()
    state.index += 1

    if state.index > len(state.card_order) - 1:
        state.index = 0

    session.commit()
    return {}


def current():
    session = db.session
    state = session.query(State).first()
    index = state.index
    card_number = state.card_order[index]
    card = session.query(Cards).where(Cards.number == card_number).first()
    return card.to_dict()
