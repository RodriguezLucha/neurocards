from api.models.models import db
from api.routes.cards import cards, cards_id, piles
from api.routes.iteration import (
    current,
    flip,
    hide,
    next,
    previous,
    reset,
    seed,
    shuffle,
    switch_pile,
)
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate  # type: ignore

app = Flask(__name__)
CORS(app)


@app.route("/cards")
def route_cards():
    return cards()


@app.route("/piles")
def route_piles():
    return piles()


@app.route("/switch/<pile>")
def route_switch_pile(pile):
    return switch_pile(pile)


@app.route("/cards/<int:id>")
def route_cards_id(id):
    return cards_id(id)


@app.route("/seed")
def route_seed():
    return seed()


@app.route("/next")
def route_next():
    return next()


@app.route("/flip")
def route_flip():
    return flip()


@app.route("/hide")
def route_hide():
    return hide()


@app.route("/shuffle")
def route_shuffle():
    return shuffle()


@app.route("/reset")
def route_reset():
    return reset()


@app.route("/previous")
def route_previous():
    return previous()


@app.route("/current")
def route_current():
    return current()


app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:password@localhost/neurocards"
)
migrate = Migrate(app, db)
db.init_app(app)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5003)
