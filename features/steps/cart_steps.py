import time
from behave import *
from selenium.webdriver.common.by import By
from locator import elem
from data import inputan

#Detail products
@then(u'I click products')
def step_impl(context):
    context.driver.find_element(By.XPATH, elem.cart_product_btn).click()

@then(u'Click linktext back products')
def step_impl(context):
    context.driver.find_element(By.ID, elem.cart_backtoproduct_btn).click()

@then(u'I back to list products')
def step_impl(context):
    status = context.driver.find_element(By.XPATH, elem.verify_login_valid2).is_displayed()  
    status = context.driver.find_element(By.XPATH, elem.cart_product_backpack).is_displayed()  
    assert status is True


#Add to cart & remove
@then(u'Click button add to cart')
def step_impl(context):
    context.driver.find_element(By.ID, elem.addtocart_btn).click()


@then(u'Click icon cart')
def step_impl(context):
    context.driver.find_element(By.CLASS_NAME, elem.shoppingcart_icon).click()


@then(u'Remove product in cart')
def step_impl(context):
    context.driver.find_element(By.ID, elem.remove_btn).click()


@then(u'Successfully add to cart and remove products in cart')
def step_impl(context):
    status = context.driver.find_element(By.XPATH, elem.cart_verify_remove).is_displayed()  
    assert status is True


#Multiple add to cart
@then(u'Click continue shopping button')
def step_impl(context):
    context.driver.find_element(By.ID, elem.cart_continueshopping_btn).click()


@then(u'I click other products')
def step_impl(context):
    context.driver.find_element(By.XPATH, elem.cart_product_bikelight).click()


@then(u'Click button add to cart other product')
def step_impl(context):
    context.driver.find_element(By.ID, elem.addtocart_bikelight_btn).click()


@then(u'Remove other product in cart')
def step_impl(context):
    context.driver.find_element(By.ID, elem.remove_bikelight_btn).click()


@then(u'Successfully multiple add to cart and remove products in cart')
def step_impl(context):
    status = context.driver.find_element(By.XPATH, elem.cart_verify_remove).is_displayed()  
    assert status is True