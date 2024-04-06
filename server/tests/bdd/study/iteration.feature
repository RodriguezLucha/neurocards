Feature: Card iteration
    In order to study all the cards
    As a user
    I should be able to iterate through all cards

    Background:
        Given the following card database
            | num | english word | portuguese word | pile |
            | 1   | the          | o               | A    |
            | 2   | car          | carro           | A    |
            | 3   | cat          | gato            | A    |
            | 4   | man          | homem           | B    |
            | 5   | woman        | mulher          | B    |
            | 6   | boy          | menino          | B    |

    Scenario: Go to next card
        Given the selected pile is B
        And the selected card is 4
        When going to the next card
        Then the selected card will be 5

    @skip
    Scenario: Go to next card when at last
        Given the selected pile is B
        And the selected card is 6
        When going to the next card
        Then the selected card will be 4

    @skip
    Scenario: Go to the previous card
        Given the selected pile is B
        And the selected card is 5
        When going to the next card
        Then the selected card will be 4

    @skip
    Scenario: Go to the previous card when at first
        Given the selected pile is B
        And the selected card is 4
        When going to the next card
        Then the selected card will be 6
