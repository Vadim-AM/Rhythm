"""Модуль содержит класс базовой страницы"""
from __future__ import annotations

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config import Config


class BasePage:
    """Класс базовой страницы. Содержит наиболее часто используемые методы"""

    def __init__(self, driver: WebDriver, timeout: int = Config.total_timeout) -> None:
        self.driver = driver
        self.url = None
        self.wait = WebDriverWait(self.driver, timeout)

    def open(self) -> BasePage:
        """Открывает заданную страницу"""
        self.driver.get(self.url)
        return self

    def find_and_click_element(self, locator: tuple, err_msg: str = "") -> BasePage:
        """Ожидает появление элемента на странице, перемещает его в
        область видимости и кликает по нему"""
        ActionChains(self.driver).move_to_element(self.wait.until(
            EC.element_to_be_clickable(locator), err_msg)).click().perform()
        return self

    def get_text(self, locator: tuple) -> None | str:
        """Возвращает текст из переданного элемента"""
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return None
        return self.driver.find_element(*locator).text
