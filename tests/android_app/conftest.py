import allure_commons
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser, support

from browserstack_sample_app_tests.utils import attach
from config import config


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # Specify device and os_version for testing
        "platformName": "android",
        "platformVersion": config.android_platform_version,
        "deviceName": config.android_device_name,

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

    attach.add_screenshot(browser)
    attach.add_xml(browser)

    session_id = browser.driver.session_id

    yield

    browser.quit()

    attach.add_video(browser, session_id)
