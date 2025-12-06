import allure

from generation import Generation
from locators.exo_box_page_locators import SettingsLocators
from pages.base_page import BasePage


class ExoBoxPage(BasePage):
    locators = SettingsLocators

    @allure.step("Открываем страницу ExoBox")
    def open_exo_box_page(self) -> None:
        self.click(self.locators.EXO_BOX)

    @allure.step("Вводим текст в поле ввода")
    def enter_message(self) -> str:
        text = Generation.text(10)
        self.send_keys(self.locators.TEXT_INPUT, text)
        return text

    @allure.step("Нажимаем кнопку Сохранить")
    def save_message(self) -> None:
        self.click(self.locators.SAVE_BUTTON)

    @allure.step("Получаем текст сохраненного сообщения")
    def get_saved_message(self) -> str:
        return self.get_text(self.locators.SAVED_MESSAGE)
