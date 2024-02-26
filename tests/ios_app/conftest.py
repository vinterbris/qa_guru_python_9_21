import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser

from config import config


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = XCUITestOptions().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "ios",
        "platformVersion": "13.0",
        "deviceName": "iPhone 11 Pro",

        # Set URL of the application under test
        "app": "bs://sample.app",

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

    browser.config.driver_remote_url = config.remote_url
    browser.config.driver_options = options

    browser.config.timeout = config.timeout

    yield

    browser.quit()