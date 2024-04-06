from app.models.models import Cards, db


def cards():
    cards = db.session.query(Cards).all()
    return [card.to_dict() for card in cards]


def cards_id(id):
    card = db.session.query(Cards).where(Cards.number == id).first()
    return card.to_dict()
