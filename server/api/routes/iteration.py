import random

from api.models.models import Cards, State, db


def next():
    session = db.session
    state = session.query(State).first()
    state.index += 1

    if state.index > len(state.card_order) - 1:
        state.index = 0

    state.show_front = True

    session.commit()
    return {}


def flip():
    session = db.session
    state = session.query(State).first()
    state.show_front = not state.show_front

    session.commit()
    return {}


def my_shuffle(arr):
    random.shuffle(arr)
    return arr


def shuffle():
    session = db.session
    state = session.query(State).first()
    state.index = 0
    state.show_front = True
    state.card_order = my_shuffle(state.card_order)
    session.add(state)
    session.commit()
    return {}


def reset():
    session = db.session
    state = session.query(State).first()
    state.index = 0
    state.show_front = True
    state.card_order = sorted(state.card_order)
    session.add(state)
    session.commit()
    return {}


def previous():
    session = db.session
    state = session.query(State).first()
    state.index -= 1

    if state.index < 0:
        state.index = len(state.card_order) - 1

    state.show_front = True

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

    return {
        "number": card.number,
        "word": word,
        "card_order": state.card_order,
    }
