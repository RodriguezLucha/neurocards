from flask import Flask

from models.models import db
from routes.cards import cards_controller

app = Flask(__name__)


@app.route("/cards", methods=["GET"])
def cards():
    return cards_controller()


app.config["SQLALCHEMY_DATABASE_URI"] = (
    "postgresql://postgres:password@localhost/neurocards"
)
db.init_app(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
