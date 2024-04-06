from flask import Flask
from flask_migrate import Migrate

from api.models.models import db
from api.routes.cards import cards, cards_id

app = Flask(__name__)


@app.route("/cards")
def route_cards():
    return cards()


@app.route("/cards/<int:id>")
def route_cards_id(id):
    return cards_id(id)


app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:password@localhost/neurocards"
)
migrate = Migrate(app, db)
db.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)