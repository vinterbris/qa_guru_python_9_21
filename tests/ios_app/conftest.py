import allure
import allure_commons
import pytest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from selene import browser, support

from browserstack_sample_app_tests.utils import attach
from config import config


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = XCUITestOptions().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "ios",
        "platformVersion": config.ios_platform_version,
        "deviceName": config.ios_device_name,

        # Set URL of the application under test
        "app": config.browserstack_app_url,

        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            # Set your access credentials
            "userName": config.USR,
            "accessKey": config.ACCESS_KEY
        }
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)

    browser.config.timeout = config.timeout
    browser.config._wait_decorator = support._logging.wait_with(context=allure_commons._allure.StepContext)

    yield

    attach.attach_screenshot()
    session_id = browser.driver.session_id

    with allure.step('Tear down app session'):
        browser.quit()

    attach.attach_bstack_video(session_id)
