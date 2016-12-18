Feature: Commandline guestbook

  Scenario: Open the guestbook
    Given there is a guestbook with signatures
        | name         | date       |
        | Rob Jones    | 10/01/2016 |
        | Stella Doe   | 07/29/2015 |

    Then a user will find "Rob Jones" there

