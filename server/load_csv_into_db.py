import csv
import os

from api.models.models import Cards, Piles, State
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

url = os.environ["POSTGRES_URL"]
csv_file_path = os.environ["CSV_PATH"]


engine = create_engine(url)
session = scoped_session(sessionmaker(bind=engine))

pile_number = 1

session.query(State).delete()
session.query(Cards).delete()
session.query(Piles).delete()
session.commit()

first = True
with open(csv_file_path, mode="r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if first:
            first = False
            continue

        count = (
            session.query(Piles)
            .where(
                Piles.pile_name == str(pile_number),
            )
            .count()
        )
        if count < 1:
            pile = Piles(pile_name=str(pile_number))
            session.add(pile)
            session.commit()

        number = row[0].strip()
        english_word = row[1].strip()
        english_sentence = row[2].strip()
        portuguese_word = row[3].strip()
        portuguese_sentence = row[4].strip()
        pile_name = str(pile_number)
        print(number)
        card = Cards(
            number=number,
            english_word=english_word,
            english_sentence=english_sentence,
            portuguese_word=portuguese_word,
            portuguese_sentence=portuguese_sentence,
            pile_name=pile_name,
        )
        session.add(card)
        session.commit()

        if (int(number) % 20) == 0:
            pile_number += 1

count = session.query(State).count()
if count < 1:
    state = State(
        index=0,
        card_order=None,
        chosen_pile_name=None,
        show_front=True,
    )
    session.add(state)
    session.commit()
