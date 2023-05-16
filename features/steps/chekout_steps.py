import time
from behave import *
from selenium.webdriver.common.by import By
from locator import elem
from data import inputan

@then(u'Click checkout buutton')
def step_impl(context):
    context.driver.find_element(By.ID, elem.checkout_btn).click()


@then(u'Input firstname "{first}", lastname "{last}", and postalcode "{code}"')
def step_impl(context, first, last, code):
    context.driver.find_element(By.ID, elem.firstname).send_keys(first) 
    context.driver.find_element(By.ID, elem.lastname).send_keys(last)
    context.driver.find_element(By.ID, elem.postalcode).send_keys(code) 


@then(u'Click continue button in checkout your information page')
def step_impl(context):
    context.driver.find_element(By.ID, elem.continue_btn).click()


@then(u'Click finish button')
def step_impl(context):
    context.driver.find_element(By.ID, elem.finish_btn).click()


@then(u'Successfully checkout')
def step_impl(context):
    assert(context.driver.find_element(By.CLASS_NAME, elem.verify_complete_checkout).text) == inputan.verify_complete_checkout


#Empty Firstname
@then(u'Input firstname "", lastname "{last}", and postalcode "{code}"')
def step_impl(context, last, code):
    context.driver.find_element(By.ID, elem.firstname).send_keys() 
    context.driver.find_element(By.ID, elem.lastname).send_keys(last)
    context.driver.find_element(By.ID, elem.postalcode).send_keys(code) 


@then(u'Should not be checkout finish and view error message firstname')
def step_impl(context):
    assert(context.driver.find_element(By.XPATH, elem.verify_checkout_error_msg_firstname).text) == inputan.verify_checkout_error_msg_firstname

#Empty Lastname
@then(u'Input firstname "{first}", lastname "", and postalcode "{code}"')
def step_impl(context, first, code):
    context.driver.find_element(By.ID, elem.firstname).send_keys(first) 
    context.driver.find_element(By.ID, elem.lastname).send_keys()
    context.driver.find_element(By.ID, elem.postalcode).send_keys(code) 

@then(u'Should not be checkout finish and view error message lastname')
def step_impl(context):
    assert(context.driver.find_element(By.XPATH, elem.verify_checkout_error_msg_lastname).text) == inputan.verify_checkout_error_msg_lastname    

#Empty Postalcode
@then(u'Input firstname "{first}", lastname "{last}", and postalcode ""')
def step_impl(context, first, last):
    context.driver.find_element(By.ID, elem.firstname).send_keys(first) 
    context.driver.find_element(By.ID, elem.lastname).send_keys(last)
    context.driver.find_element(By.ID, elem.postalcode).send_keys() 

@then(u'Should not be checkout finish and view error message postal')
def step_impl(context):
    assert(context.driver.find_element(By.XPATH, elem.verify_checkout_error_msg_postal).text) == inputan.verify_checkout_error_msg_postal  