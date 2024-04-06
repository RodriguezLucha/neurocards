from flask import Flask

import routes.cards
from models.models import db

app = Flask(__name__)


@app.route("/cards")
def route_cards():
    return routes.cards.cards()


@app.route("/cards/<int:id>")
def route_cards_id(id):
    return routes.cards.cards_id(id)


app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:password@localhost/neurocards"
)
db.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
