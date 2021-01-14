import pytest
from utils import utils as utils


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser n(me e.g. chrome OR firefox")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    browser = request.config.getoption("--browser")
    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=utils.CHROME_DRIVER_PATH)
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=utils.GECKO_DRIVER_PATH)
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver    # request.cls.driver is similar to "request.class.driver"
    yield
    driver.close()
    driver.quit()
    print("Test Completed")



