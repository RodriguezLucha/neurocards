Feature: Card hiding
    In order to focus on the cards that need attention
    As a user
    I should be able to hide already learned cards

    Background:
        Given the following card database
            | num | english word | portuguese word | pile | hidden |
            | 1   | the          | o               | A    | no     |
            | 2   | car          | carro           | A    | no     |
            | 3   | cat          | gato            | A    | no     |
            | 4   | man          | homem           | A    | no     |
            | 5   | woman        | mulher          | A    | no     |

    Scenario: Hiding an already learned card
        Given the selected pile is A
        And the selected card is 3
        When hiding the current card
        And viewing the card
        Then the selected card will be 4
        And the card order will be [1,2,4,5]
        And the card database has
            | num | english word | portuguese word | pile | hidden |
            | 1   | the          | o               | A    | no     |
            | 2   | car          | carro           | A    | no     |
            | 3   | cat          | gato            | A    | yes    |
            | 4   | man          | homem           | A    | no     |
            | 5   | woman        | mulher          | A    | no     |
    Scenario: Hiding call cards in the pile
        Given the selected pile is A
        And the selected card is 1
        When hiding the current card
        And hiding the current card
        And hiding the current card
        And hiding the current card
        And hiding the current card
        And viewing the card
        Then the selected card will be 0

