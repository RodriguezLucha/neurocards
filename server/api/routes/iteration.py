import random

from api.models.factories import StateFactory  # type: ignore
from api.models.models import Cards, Piles, State, db  # type: ignore


def seed():
    session = db.session
    session.query(State).delete()
    session.query(Cards).delete()
    session.query(Piles).delete()

    def add_pile(name):
        pile = Piles(pile_name=name)
        session.add(pile)
        session.commit()

    add_pile("A")
    add_pile("B")

    def add_card(num, eng_word, eng_sen, por_word, por_sen, pile):
        card = Cards(
            number=num,
            english_word=eng_word,
            english_sentence=eng_sen,
            portuguese_word=por_word,
            portuguese_sentence=por_sen,
            pile_name=pile,
            hidden=False,
        )
        session.add(card)
        session.commit()

    add_card(1, "the", "the man", "o", "o homem", "A")
    add_card(2, "dog", "the dog", "cachorro", "o cachorro", "A")
    add_card(3, "cat", "the cat", "gato", "o gato", "A")
    add_card(4, "man", "the man", "homem", "o homem", "A")
    add_card(5, "black", "black cat", "preto", "gato preto", "A")
    add_card(6, "keys", "the keys", "chaves", "o chaves", "A")
    add_card(
        7, "good night", "good night sir", "boa noite", "boa noite senhor", "B"
    )  # noqa
    add_card(8, "thank you", "thank you cat", "obrigado", "obrigado gato", "B")
    add_card(
        9,
        "you're welcome",
        "you're welcome ma'am",
        "de nada",
        "de nada senhora",
        "B",  # noqa
    )

    state = StateFactory()
    session.add(state)
    session.commit()
    switch_pile("A")

    return {}


def remove_element(array, index):
    return array[:index] + array[index + 1 :]  # noqa


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

    if len(state.card_order) == 0:
        state.index = 0
        state.card_order = None
        state.chosen_pile_name = None
        state.show_front = True
        session.add(state)
        session.commit()
        return {}

    if state.index > len(state.card_order) - 1:
        state.index = 0  # pragma: no cover

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


def my_shuffle(arr):  # pragma: nocover
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

    if state.chosen_pile_name is None:  # pragma: no cover
        return {
            "number": 0,
            "word": "-",
            "sentence": "-",
            "card_order": [],
            "front": True,
            "pile": "-",
        }

    index = state.index
    card_number = state.card_order[index]
    card = session.query(Cards).where(Cards.number == card_number).first()

    word = card.english_word
    sentence = card.english_sentence
    pile = card.pile_name
    if not state.show_front:
        word = card.portuguese_word
        sentence = card.portuguese_sentence

    return {
        "number": card.number,
        "word": word,
        "sentence": sentence,
        "card_order": state.card_order,
        "front": state.show_front,
        "pile": pile,
    }


def switch_pile(pile):
    session = db.session
    state = session.query(State).first()
    state.chosen_pile_name = pile
    cards = (
        session.query(Cards)
        .where((Cards.pile_name == pile) & (Cards.hidden == False))
        .all()
    )
    card_numbers = [x.number for x in cards]
    state.index = 0
    state.show_front = True
    state.card_order = sorted(card_numbers)
    session.add(state)
    session.commit()
    return {}
