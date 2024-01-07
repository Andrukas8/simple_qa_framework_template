from behave import *
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By


@given(u'User is on registration page')
def step_impl(context):
    context.driver.get("https://www.thetestingworld.com/testings/")


@when(u'User enters username')
def step_impl(context):
    context.driver.find_element(By.NAME, "fld_username").send_keys("User1")


@when(u'User enters email id')
def step_impl(context):
    context.driver.find_element(By.NAME, "fld_email").send_keys("abcd@gmail.com")


@when(u'User enters password')
def step_impl(context):
    context.driver.find_element(By.NAME, "fld_password").send_keys("password1")


@when(u'User clicks Signup button')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//input[@type='submit' and @value='Sign up']").click()


@then(u'User should be registered successfully')
def step_impl(context):
    print("Registered")


@given(u'User is on Registration page again')
def step_impl(context):
    context.driver.get("https://www.thetestingworld.com/testings/")


@when(u'User enters duplicate username')
def step_impl(context):
    print("Not registered")


@when(u'userAnd User enters email id')
def step_impl(context):
    print("Not registered")


@then(u'User should not be registered')
def step_impl(context):
    print("Not registered")
