Feature: Card assignment
    In order to group cards into piles to reduce load
    As a user
    I should be able to move cards into different piles

  Scenario: Card assignments
    Given piles A, B, C already exist
    And the following existing cards
      | num | english word | portuguese word | pile |
      |   1 | the          | o               |      |
      |   2 | car          | carro           | B    |
      |   3 | cat          | gato            |      |
    When assigning card 1 to pile A
    And assigning card 2 to pile C
    Then there are the folling card to pile assignments
      | card num | pile |
      |        1 | A    |
      |        2 | C    |
      |        3 |      |

  Scenario: Card unassignment
    Given piles A, B already exist
    And the following existing cards
      | num | english word | portuguese word | pile |
      |   1 | the          | o               | A    |
      |   2 | car          | carro           | A    |
    When removing card 1 from the pile
    Then there are the folling card to pile assignments
      | card num | pile |
      |        1 |      |
      |        2 | A    |
