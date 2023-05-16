Feature: Login Feature

    Background: 
        Given I am on the login page
        

Scenario: Success login with correct credential
    When I fill my credential "standard_user" and "secret_sauce"
    Then I should be login

 Scenario: Failed login with invalid user name
     When I fill wrong username "standard" and "secret_sauce"
     Then I should not be login

 Scenario: Failed login with invalid password
     When I fill wrong password "standard_user" and "secret_sauc"
     Then I should not be login

Scenario: Success logout dashboard
    When I fill my credential "standard_user" and "secret_sauce"
    Then I should be login
    Then I click humberger button and logout button in sidebar menu
    Then I sucessfuly logout

  