Feature: Pile management
            In order to sort cards into piles to reduce load
                As a user
            I should be create, read, update, and delete piles

    @skip
    Scenario: Create piles
        Given no piles are created
        When creating piles A, B
        Then piles A, B exist

    @skip
    Scenario: Edit pile
        Given piles A, B, C already exist
        When renaming pile B to pile Z
        Then piles A, Z, C exist

    @skip
    Scenario: Delete pile
        Given piles A, B, C already exist
        When deleting pile A
        Then piles B, C exist
