import random

from api.models.models import Cards, State, db


def remove_element(array, index):
    if 0 <= index < len(array):
        return array[:index] + array[index + 1 :]  # noqa
    else:
        raise ValueError("Index out of range")


def hide():
    session = db.session
    state = session.query(State).first()

    # hide the current card
    index = state.index
    card_number = state.card_order[index]
    card = session.query(Cards).where(Cards.number == card_number).first()
    card.hidden = True
    session.commit()

    # update order
    state.card_order = remove_element(state.card_order, index)

    if state.index > len(state.card_order) - 1:
        state.index = 0

    state.show_front = True

    session.commit()
    return {}


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

    if state.chosen_pile_name is None:
        return {
            "number": 0,
            "word": "-",
            "sentence": "-",
            "card_order": [],
            "front": True,
        }

    index = state.index
    card_number = state.card_order[index]
    card = session.query(Cards).where(Cards.number == card_number).first()

    word = card.english_word
    sentence = card.english_sentence
    if not state.show_front:
        word = card.portuguese_word
        sentence = card.portuguese_sentence

    return {
        "number": card.number,
        "word": word,
        "sentence": sentence,
        "card_order": state.card_order,
        "front": state.show_front,
    }


def switch_pile(pile):
    session = db.session
    state = session.query(State).first()
    state.chosen_pile_name = pile
    cards = session.query(Cards).where(Cards.pile_name == pile).all()
    card_numbers = [x.number for x in cards]
    state.index = 0
    state.show_front = True
    state.card_order = sorted(card_numbers)
    session.add(state)
    session.commit()
    return {}
