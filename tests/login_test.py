# from selenium import webdriver

from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import time
import pytest
import allure


# To run the pytest, go to the location of AutomationFramework_1 and type "pytest -v"
# Once pytest-html is installed in File > Settings > Python Interpreter, run the pytest
#    by typing "pytest --html=reports/report1.html --self-contained-html"

# Since in conftest.py, this function has been added:

# def pytest_addoption(parser):
#    parser.addoption("--browser", action="store", default="chrome", help="Type in browser n(me e.g. chrome OR firefox")

# You may run your pytest using either chrome or firefox.
#   pytest --html=reports/report3.html --self-contained-html --browser chrome
#   OR
#   pytest --html=reports/report3.html --self-contained-html --browser firefox


# To generate allure-reports,
# 1) Install allure-pytest in File > Settings > Python Interpreter
# 2) To generate an allure-report, type: pytest --alluredir=reports/allure-reports
# 3) To view the allure report:
#    3.a) Install nodeJS npm in your computer.
#    3.b) Install allure-commandline. In cmd, type: npm install -g allure-commandline --save-dev
#    3.c) To view the allure report, go back to cmd and type: allure serve reports/allure-reports

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver = self.driver  # self.driver is the same driver as the request.cls.driver from conftest.py
        driver.get(utils.URL)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        login.enter_password(utils.PASSWORD)
        login.click_login()

    def test_logout(self):
        try:
            driver = self.driver
            time.sleep(2)
            homepage = HomePage(driver)
            homepage.click_welcome()
            time.sleep(2)
            homepage.click_logout()
            actual_title = driver.title
            expected_title = "OrangeHRM"
            assert actual_title == expected_title
            test_name = utils.whoami()
            utils.take_screenshot_test_pass(driver, test_name)

        except AssertionError as error:
            print("Assertion error occurred.")
            print(error)
            test_name = utils.whoami()
            utils.take_screenshot_test_fail(driver, test_name)
            raise

        except:
            print("There was an exception.")
            # test_name = utils.whoami()
            # screenshot_name = "TEST FAIL_" + test_name + "_" + utils.current_time
            # allure.attach(driver.get_screenshot_as_png(), name=screenshot_name,
            #               attachment_type=allure.attachment_type.PNG)
            # screenshot_path = utils.SCREENSHOT_PATH + screenshot_name + ".png"
            # driver.get_screenshot_as_file(screenshot_path)
            test_name = utils.whoami()
            utils.take_screenshot_test_fail(driver, test_name)

            raise

        else:
            print("No exceptions occurred")

        finally:
            print("I am inside finally block.")
