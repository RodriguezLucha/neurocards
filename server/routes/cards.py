from models.models import Cards, db


def cards_controller():
    cards = db.session.query(Cards).all()
    return [card.to_dict() for card in cards]
