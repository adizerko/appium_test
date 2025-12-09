from appium.webdriver.common.appiumby import AppiumBy

class LoginScreenLocators:
    LOGIN_SCREEN  = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='listItemTitle' and @text='Login Screen']")
    USERNAME_INPUT = (AppiumBy.ACCESSIBILITY_ID, "username")
    PASSWORD_INPUT = (AppiumBy.ACCESSIBILITY_ID, "password")
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "loginBtn")
    INVALID_LOGIN = (AppiumBy.XPATH, "//android.widget.TextView[@resource-id='android:id/message']")
    OK_BUTTON = (AppiumBy.XPATH, "//android.widget.Button[@resource-id='android:id/button1']")

