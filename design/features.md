# Features

1. Create card with front and back (DONE)
    * Should support multi-line content
    * Should support centering text
    * Should support assigning a numbered index (DONE)
    * Ability to edit card content (DONE)
    * Ability to delete cards (DONE)

1. Should support piles
    * Ability to create, edit, delete piles
    * All cards should go to a default pile if not assigned
    * Cards should be assignable to different piles

1. Ability to practice a pile
    * Select the pile to practice (DONE)
    * Iterate through all cards in order (No cards missed)
    * Ability to flip a card
    * Ability to go to previous card
    * Ability to go to next card
    * Ability to hide the current card
    * Ability to shuffle order of cards

## REST APIs
```
POST /card
GET /card/{id}
PATCH /card/{id}
DELETE /card/{id}
PATCH /assign_card

POST /pile
GET /pile/{id}
PATCH /pile/{id}
DELETE /pile/{id}

POST /select_pile
GET /current
PATCH /flip
PATCH /next
PATCH /previous
PATCH /shuffle
PATCH /hide
```

```
CREATE TABLE Cards (
    number SERIAL PRIMARY KEY,
    english_word TEXT,
    english_sentence TEXT,
    portuguese_word TEXT,
    portuguese_sentence TEXT
);

CREATE TABLE Piles (
    pile_name TEXT PRIMARY KEY
);

CREATE TABLE State (
    index INT NOT NULL DEFAULT 0,
    cards_order INT[] NOT NULL DEFAULT '{}',
    chosen_pile TEXT REFERENCES Piles(pile_name),
    PRIMARY KEY (index)
);

```