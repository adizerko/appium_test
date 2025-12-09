import allure
from appium import webdriver

from data.login_screen_data import INVALID_LOGIN_MESSAGE
from pages.login_scren_page import LoginScreenPage


@allure.feature("Login Screen")
class TestLoginScreen:

    @allure.title("test login")
    def test_login(self, driver: webdriver) -> None:
        login_screen_page = LoginScreenPage(driver)
        login_screen_page.open_login_screen()

        login_screen_page.set_username()
        login_screen_page.set_password()
        login_screen_page.tap_login_button()

        invalid_login_message = login_screen_page.get_text_invalid_login()

        assert invalid_login_message == INVALID_LOGIN_MESSAGE, \
            f"Текст не совпадает! ОР: '{INVALID_LOGIN_MESSAGE}', ФР: '{invalid_login_message}'"
