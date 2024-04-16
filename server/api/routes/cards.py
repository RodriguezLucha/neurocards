from api.models.models import Cards, db  # type: ignore


def cards():
    cards = db.session.query(Cards).all()
    return [card.to_dict() for card in cards]


def piles():
    piles = (
        db.session.query(Cards.pile_name)
        .where(Cards.hidden.is_(False))
        .group_by(Cards.pile_name)
    ).all()

    def func(x):
        return int(x[0])

    piles = sorted(piles, key=func)
    return [pile[0] for pile in piles]


def cards_id(id):
    card = db.session.query(Cards).where(Cards.number == id).first()
    return card.to_dict()
