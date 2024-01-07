import pytest
from Base import InitiateDriver
from Pages import RegistrationPage
import time
from DataGenerate import DataGen


@pytest.mark.parametrize('data',DataGen.dataGenerator())
def test_ValidateRegistration(data):
    driver = InitiateDriver.startBrowser()
    register = RegistrationPage.RegistrationClass(driver)
    register.enter_username(data[0])
    register.enter_password(data[1])
    time.sleep(1)
    driver.close()
