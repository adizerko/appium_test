import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture
def capabilities() -> dict[str, str] :
    return dict(
        platformName='Android',
        automationName='uiautomator2',
        deviceName='Android',
        appPackage='com.appiumpro.the_app',
        appActivity='.MainActivity',
        language='en',
        locale='US'
    )


@pytest.fixture
def driver(capabilities: dict[str, str]):
    options = UiAutomator2Options()
    options.load_capabilities(capabilities)

    driver = webdriver.Remote("http://localhost:4723", options=options)
    yield driver
    driver.quit()
