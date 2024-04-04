Feature: Card management
    In order to study cards
    As a user
    I should be able to create, read, update, and delete cards

  Scenario: Create cards
    Given no cards are created
    When creating cards
      | num | english word | portuguese word |
      |   1 | the          | o               |
    Then 1 card is created

  Scenario: Edit card
    Given the following existing cards
      | num | english word | portuguese word |
      |   1 | the          | o               |
      |   2 | car          | carro           |
    When updating card 2 with the following values
      | english word | portuguese word |
      | cat          | gato            |
    Then the following cards exist
      | num | english word | portuguese word |
      |   1 | the          | o               |
      |   2 | cat          | gato            |

  Scenario: Delete card
    Given the following existing cards
      | num | english word | portuguese word |
      |   1 | the          | o               |
      |   2 | car          | o               |
    When deleting card 1
    Then the following cards exist
      | num | english word | portuguese word |
      |   2 | cat          | o               |