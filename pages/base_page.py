import allure
from appium import webdriver
from appium.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: webdriver):
        self.driver = driver

    @allure.step("Ждем видимость элемента: {locator}")
    def wait_visible(self, locator: tuple[str, str], timeout: int = 10) -> WebElement:
        element = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator))
        return  element

    @allure.step("Вводим текст '{keys}' в элемент: {locator}")
    def send_keys(self, locator: tuple[str, str], keys: str, timeout: int = 10) -> None:
        el = self.wait_visible(locator, timeout)
        el.clear()
        el.send_keys(keys)

    @allure.step("Кликаем по элементу: {locator}")
    def click(self, locator: tuple[str, str], timeout: int = 10) -> None:
        el = self.wait_visible(locator, timeout)
        el.click()

    @allure.step("Получаем текст элемента: {locator}")
    def get_text(self, locator: tuple[str, str], timeout: int = 10) -> str:
        return self.wait_visible(locator, timeout).text
