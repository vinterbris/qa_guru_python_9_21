from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search():
    with step('Нажать на поле ввода'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Button")).click()
    with step('Ввести значение и подтвердить'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).send_keys('Allure' + '\n')
    with step('Проверить наличие значения в списке'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text("Allure"))