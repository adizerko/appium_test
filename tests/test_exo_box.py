import allure
from appium.webdriver.webdriver import WebDriver

from pages.exo_box_page import ExoBoxPage


@allure.feature("ExoBox")
class TestExoBox:

    @allure.story("Сохранение сообщения и проверка")
    def test_exo_box(self, driver: WebDriver) -> None:
        exo_box_page = ExoBoxPage(driver)
        exo_box_page.open_exo_box_page()
        message_to_save = exo_box_page.enter_message()
        exo_box_page.save_message()
        saved_message = exo_box_page.get_saved_message()

        assert message_to_save == saved_message, \
            f"Текст не совпадает! Введено: '{message_to_save}', сохранено: '{saved_message}'"
