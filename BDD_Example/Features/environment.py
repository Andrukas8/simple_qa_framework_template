from selenium import webdriver
from selenium.webdriver import Chrome


def before_scenario(context,scenario):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    context.driver = Chrome(options=options)


def after_scenario(context,scenario):
    context.driver.close()
