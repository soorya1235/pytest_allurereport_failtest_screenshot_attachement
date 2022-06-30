import allure
from allure_commons.types import AttachmentType
import pytest
from selenium import webdriver

@pytest.fixture()
def log_on_failure(request, chrome_browser):
    yield
    item = request.node
    driver = chrome_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)

def get_data():
    return [
        ("trainer@way2automation.com","abcd"),
        ("soorya","choti"),
        ("sadfasfd","sadfsadf")
    ]

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("username,password",get_data())
def test_login(username,password,chrome_browser):
    driver = chrome_browser
    driver.find_element_by_id("email").send_keys("username")
    driver.find_element_by_id("pass").send_keys("password")
    #allure.attach(driver.get_screenshot_as_png(),name="dologin", attachment_type=AttachmentType.PNG)
    assert 1 == 2