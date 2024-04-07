from api.models.models import Cards, State, db


def next():
    session = db.session
    state = session.query(State).first()
    state.index += 1

    if state.index > len(state.card_order) - 1:
        state.index = 0

    session.commit()
    return {}


def flip():
    session = db.session
    state = session.query(State).first()
    state.show_front = not state.show_front

    session.commit()
    return {}


def previous():
    session = db.session
    state = session.query(State).first()
    state.index -= 1

    if state.index < 0:
        state.index = len(state.card_order) - 1

    session.commit()
    return {}


def current():
    session = db.session
    state = session.query(State).first()
    index = state.index
    card_number = state.card_order[index]
    card = session.query(Cards).where(Cards.number == card_number).first()
    word = card.english_word
    if not state.show_front:
        word = card.portuguese_word

    return {"number": card.number, "word": word}
