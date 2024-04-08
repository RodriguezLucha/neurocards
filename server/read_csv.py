import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from api.models.models import Cards, Piles, State

url = "postgresql://postgres:password@localhost/neurocards"
engine = create_engine(url)
session = scoped_session(sessionmaker(bind=engine))
csv_file_path = "/Users/rudy/Documents/flashcards.csv"
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

        count = session.query(Piles).where(Piles.pile_name == str(pile_number)).count()
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
