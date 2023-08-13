"""Содержит класс главной страницы"""
from selenium.webdriver.common.by import By

from config import Hosts
from pages.base_page import BasePage
from pages.elements_page import ElementsPage
from src.texts import ErrMsg


class MainPage(BasePage):
    """Содержит локаторы и методы страницы Elements"""
    ELEMENTS_BUTTON = (By.XPATH, "//div/h5[text()='Elements']")

    def open_an_elements_page(self) -> ElementsPage:
        """Открывает главную страницу и нажимает кнопку Elements"""
        self.url = Hosts.demo_qa_host
        self.open() \
            .find_and_click_element(self.ELEMENTS_BUTTON, ErrMsg.elements_button_not_found)
        return ElementsPage(self.driver)
