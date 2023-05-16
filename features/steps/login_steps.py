import time
from behave import *
from selenium.webdriver.common.by import By
from locator import elem
from data import inputan


@given(u'I am on the login page')
def step_impl(context):
    context.driver.get(inputan.baseUrl)
    assert(context.driver.title) == inputan.verify_title_homepage


@when(u'I fill my credential "{username}" and "{password}"')
def step_impl(context, username, password):
    context.driver.find_element(By.ID, elem.username).send_keys(username) 
    context.driver.find_element(By.ID, elem.password).send_keys(password)
    context.driver.find_element(By.ID, elem.login_btn).click()


@then(u'I should be login')
def step_impl(context):
    #Validation Option 1
    status = context.driver.find_element(By.XPATH, elem.verify_login_valid).is_displayed()
    assert status is True
    
    #Validation Option 2
    assert(context.driver.find_element(By.XPATH, elem.verify_login_valid2).text) == inputan.verify_login_valid

  
#wrong username
@when(u'I fill wrong username "{usernamewrong}" and "{password}"')
def step_impl(context, usernamewrong, password):
    context.driver.find_element(By.ID, elem.username).send_keys(usernamewrong) 
    context.driver.find_element(By.ID, elem.password).send_keys(password)
    context.driver.find_element(By.ID, elem.login_btn).click()

@then(u'I should not be login')
def step_impl(context):
    assert(context.driver.find_element(By.XPATH, elem.error_msg_login).text) == inputan.verify_error_login
    


#wrong password
@when(u'I fill wrong password "{username}" and "{passwordwrong}"')
def step_impl(context, username, passwordwrong):
    context.driver.find_element(By.ID, elem.username).send_keys(username) 
    context.driver.find_element(By.ID, elem.password).send_keys(passwordwrong)
    context.driver.find_element(By.ID, elem.login_btn).click()


#logout
@then(u'I click humberger button and logout button in sidebar menu')
def step_impl(context):
    context.driver.find_element(By.ID, elem.burger_btn).click()
    time.sleep(2)
    context.driver.find_element(By.ID, elem.logout_btn).click()

@then(u'I sucessfuly logout')
def step_impl(context):
    status = context.driver.find_element(By.CLASS_NAME, elem.title_homepage).is_displayed()
    assert status is True