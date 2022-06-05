import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service



@pytest.fixture ()
def test_initiateBrowser22():
    global driver
    s = Service ( "../pytest_training_and_gihtup/driver_settings/chromedriver3" )
    driver = webdriver.Chrome ( service=s )
    driver.implicitly_wait ( 5 )
    driver.get ( 'https://www.facebook.com/' )
    driver.maximize_window ()
    driver.implicitly_wait ( 20 )
    yield
    driver.close ()


@pytest.mark.skip ( 'regression' )
def testing_system(test_initiateBrowser22):
    driver.find_element_by_name ( 'email' ).send_keys ( 'omid is omid' )
    assert driver.title == 'Facebook - log in or sign up'

@pytest.mark.skip ( 'regression' )
def testing_system1(test_initiateBrowser22):
    driver.find_element_by_name ( 'pass' ).send_keys ( 'whataworldishere' )
    driver.get_screenshot_as_file ( '../Pytest/Login_ScreenShot/test11.png' )

@pytest.mark.skip ( 'regression' )
def testing_system2(test_initiateBrowser22):
    driver.find_element_by_xpath ( "//*[text()='Forgot password?']" ).click ()
    driver.get_screenshot_as_file ( '../Pytest/Login_ScreenShot/test12.png' )


def test12_one(test_initiateBrowser22):
    driver.find_element_by_name ( 'email' ).send_keys ( 'omid is omid' )
    assert driver.title == 'Facebook - log in or sign up'


def test_1(test_initiateBrowser22):
    name = "Selenium"
    title = "Selenium is powerful tool"
    assert name in title

def test_2():
    name = "Jenkins"
    title = "Jenkins runner machine"
    assert name in title, "title does not match"
