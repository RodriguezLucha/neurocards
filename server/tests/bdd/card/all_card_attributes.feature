Feature: Card supports multiple attributes
    In order to make Portugues easier to learn
    As a user
    I should be able to specify multiple attributes
    such as an additional context

  Scenario: Create a card that has a word and sentence
    Given no cards are created
    When creating a card with all attributes filled in
      | attribute           | value   |
      | num                 |       1 |
      | english word        | the     |
      | portuguese word     | o       |
      | english sentence    | the car |
      | portuguese sentence | o carro |
    Then card 1 has the following values
      | attribute           | value   |
      | num                 |       1 |
      | english word        | the     |
      | portuguese word     | o       |
      | english sentence    | the car |
      | portuguese sentence | o carro |
