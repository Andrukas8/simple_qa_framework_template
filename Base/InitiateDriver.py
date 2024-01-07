from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from selenium import webdriver
from Library import ConfigReader

def startBrowser():
    global driver

    if(ConfigReader.readConfigData('Details','Application_URL')=="chrome"):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = Chrome(options=options)
    elif(ConfigReader.readConfigData('Details','Application_URL')=="firefox"):
        driver = Firefox()
    else:
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        driver = Chrome(options=options)

    driver.get(ConfigReader.readConfigData('Details','Application_URL'))
    driver.maximize_window()
    return driver

def closeBrowser():
    driver.close()