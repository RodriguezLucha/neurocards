Feature: Card shuffling
    In order fully commit cards to memory
    As a user
    I should be able to the currently focused pile

  Background: 
    Given the following card database
      | num | english word | portuguese word | pile |
      |   1 | the          | o               | A    |
      |   2 | car          | carro           | A    |
      |   3 | cat          | gato            | A    |
      |   4 | man          | homem           | A    |
      |   5 | woman        | mulher          | A    |

  Scenario: Shuffling the current pile
    Given the selected pile is A
    And the selected card is 3
    When shuffling the pile with the reverse strategy
    Then the card order will be [5, 4, 3, 2, 1]
    And the current card will 5