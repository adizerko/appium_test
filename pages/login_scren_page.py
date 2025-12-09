import allure

from generation import Generation
from locators.login_scren_page_locators import LoginScreenLocators
from pages.base_page import BasePage


class LoginScreenPage(BasePage):
    locators = LoginScreenLocators

    @allure.step("Открытие экрана логина")
    def open_login_screen(self):
        self.click(self.locators.LOGIN_SCREEN)

    @allure.step("Ввод имени пользователя")
    def set_username(self) -> None:
        self.send_keys(self.locators.USERNAME_INPUT, Generation.username())

    @allure.step("Ввод пароля")
    def set_password(self) -> None:
        self.send_keys(self.locators.PASSWORD_INPUT, Generation.password())

    @allure.step("Нажатие кнопки Login")
    def tap_login_button(self) -> None:
        self.click(self.locators.LOGIN_BUTTON)

    @allure.step("Получение текста ошибки некорректного логина")
    def get_text_invalid_login(self) -> str:
        invalid_login_text = self.get_text(self.locators.INVALID_LOGIN)
        return invalid_login_text
