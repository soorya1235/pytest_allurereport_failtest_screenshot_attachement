from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

#global driver

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="session")
def chrome_browser():
    global driver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("http://facebook.com")
    driver.maximize_window()
    yield driver
    driver.close()