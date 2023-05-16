Feature: Checkout Feature

    Background:
        Given I am on the login page
        When I fill my credential "standard_user" and "secret_sauce"
        Then I should be login 
        Then I click products
        Then Click button add to cart 
        Then Click icon cart
        Then Click checkout buutton


Scenario: Success add to cart & Checkout
    Then Input firstname "Andi", lastname "Efendi", and postalcode "16954"
    Then Click continue button in checkout your information page
    Then Click finish button
    Then Successfully checkout 
  
Scenario: Failed add to cart & Checkout with empty firstname 
    Then Input firstname "", lastname "Efendi", and postalcode "16954"
    Then Click continue button in checkout your information page
    Then Should not be checkout finish and view error message firstname  

Scenario: Failed add to cart & Checkout with empty lastname 
    Then Input firstname "Andi", lastname "", and postalcode "16954"
    Then Click continue button in checkout your information page
    Then Should not be checkout finish and view error message lastname  

Scenario: Failed add to cart & Checkout with empty postalcode 
    Then Input firstname "Andi", lastname "Efendi", and postalcode ""
    Then Click continue button in checkout your information page
    Then Should not be checkout finish and view error message postal  