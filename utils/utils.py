#CONSTANTS
import moment
import inspect
import allure

URL      = "https://opensource-demo.orangehrmlive.com/"
USERNAME = "Admin"
PASSWORD = "admin123"
GECKO_DRIVER_PATH  = "C:/Users/Zeta Dart Lap 2/PycharmProjects/AutomationFramework_1/drivers/geckodriver.exe"
CHROME_DRIVER_PATH = "C:/Users/Zeta Dart Lap 2/PycharmProjects/AutomationFramework_1/drivers/chromedriver.exe"
SCREENSHOT_PATH = "C:/Users/Zeta Dart Lap 2/PycharmProjects/AutomationFramework_1/screenshots/"
current_time = moment.now().strftime("%m-%d-%Y_%H-%M-%S")

def whoami():
    return inspect.stack()[1][3]

def take_screenshot_test_pass(driver, test_name):
    screenshot_name = "TEST PASS_" + test_name + "_" + current_time
    allure.attach(driver.get_screenshot_as_png(), name=screenshot_name,
                  attachment_type=allure.attachment_type.PNG)
    screenshot_path = SCREENSHOT_PATH + screenshot_name + ".png"
    driver.get_screenshot_as_file(screenshot_path)

def take_screenshot_test_fail(driver, test_name):
    screenshot_name = "TEST FAIL_" + test_name + "_" + current_time
    allure.attach(driver.get_screenshot_as_png(), name=screenshot_name,
                  attachment_type=allure.attachment_type.PNG)
    screenshot_path = SCREENSHOT_PATH + screenshot_name + ".png"
    driver.get_screenshot_as_file(screenshot_path)


