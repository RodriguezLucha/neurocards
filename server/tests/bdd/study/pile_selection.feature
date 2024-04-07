Feature: Pile selection
    In to limit focus to a subset of cards
    As a user
    I should be able to select a specific pile to focus effort on learning

    Background:
        Given the following card database
            | num | english word | portuguese word | pile |
            | 1   | the          | o               | A    |
            | 2   | car          | carro           | A    |
            | 3   | boy          | menino          | B    |
            | 4   | cat          | gato            | B    |

    Scenario: Select the first pile to study
        Given no pile is selected
        When selecting pile B
        And viewing the card
        Then the card number is 3
        And the card order will be [3,4]

    Scenario: Select another pile after one is selected
        Given the selected pile is B
        When selecting pile A
        And viewing the card
        Then the card number is 1

    @skip
    Scenario: Unset the selected pile
        Given the selected pile is A
        When unsetting the selected pile
        Then no card should be selected
