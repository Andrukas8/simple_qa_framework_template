from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from Base import InitiateDriver
import time
from Base import InitiateDriver
from Library import ConfigReader

def test_registration_invalid_data():
    driver = InitiateDriver.startBrowser()
    time.sleep(1)
    driver.close()