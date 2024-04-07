from api.models.models import Cards


def test_seed(clear, client, session):
    res = client.get("/seed")
    assert res.status_code == 200
    cards = session.query(Cards).all()
    assert len(cards) == 9
