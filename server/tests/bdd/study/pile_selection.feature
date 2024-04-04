Feature: Pile selection
  In to limit focus to a subset of cards
  As a user
  I should be able to select a specific pile to focus effort on learning

  Background: 
    Given the following existing cards and piles
      | num | english word | portuguese word | pile |
      |   1 | the          | o               | A    |
      |   2 | car          | carro           | A    |
      |   3 | boy          | menino          | B    |
      |   4 | cat          | gato            | B    |

  Scenario: Select the first pile to study
    Given no pile is selected
    When selecting pile B
    Then the selected card should be 3 facing the front

  Scenario: Select another pile after one is selected
    Given the selected pile is B
    When selecting pile A
    Then the selected card should be 1 facing the front

  Scenario: Unset the selected pile
    Given the selected pile is A
    When unsetting the selected pile
    Then no card should be selected
