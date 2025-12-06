from appium.webdriver.common.appiumby import AppiumBy


class SettingsLocators:
    EXO_BOX = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="listItemTitle" and @text="Echo Box"]')
    SAVE_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@text="Save"]')
    TEXT_INPUT = (AppiumBy.ACCESSIBILITY_ID, "messageInput")
    SAVED_MESSAGE = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("savedMessage")')
