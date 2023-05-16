Feature: Products Feature

    Background:
        Given I am on the login page
        When I fill my credential "standard_user" and "secret_sauce"
        Then I should be login 
        Then I click products
        

Scenario: Detail products 
    Then Click linktext back products
    Then I back to list products
    

Scenario: Add to cart & remove
    Then Click button add to cart 
    Then Click icon cart
    Then Remove product in cart
    Then Successfully add to cart and remove products in cart 

Scenario: Multiple add to cart & remove
    Then Click button add to cart 
    Then Click icon cart
    Then Click continue shopping button
    Then I click other products 
    Then Click button add to cart other product 
    Then Click icon cart
    Then Remove product in cart
    Then Remove other product in cart
    Then Successfully multiple add to cart and remove products in cart 