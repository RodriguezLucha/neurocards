Feature: Card iteration
    In order to study all the cards
    As a user
    I should be able to iterate through all cards

  Background: 
    Given the following card database
      | num | english word | portuguese word | pile |
      |   1 | the          | o               | A    |
      |   2 | car          | carro           | A    |
      |   3 | cat          | gato            | A    |
      |   4 | man          | homem           | B    |
      |   5 | woman        | mulher          | B    |
      |   6 | boy          | menino          | B    |

  Scenario: Viewing front of the card
    Given the selected card is 4 and is facing the front
    When viewing the card
    Then the word is man

  Scenario: Viewing back of the card
    Given the selected card is 4 and is facing the back
    When viewing the card
    Then the word is homem

  Scenario: Flipping the front to back
    Given the selected card is 4 and is facing the front
    When flipping the card
    Then the word is homem

  Scenario: Flipping the back to front
    Given the selected card is 4 and is facing the back
    When flipping the card
    Then the word is man
