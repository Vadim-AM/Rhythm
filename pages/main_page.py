"""Содержит класс главной страницы"""
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from config import Hosts
from pages.base_page import BasePage
from pages.elements_page import ElementsPage
from src.texts import ErrMsg


class MainPage(BasePage):
    """Содержит локаторы и методы страницы Elements"""
    ELEMENTS_BUTTON = (By.XPATH, "//div/h5[text()='Elements']")

    def open_an_elements_page(self) -> ElementsPage:
        self.find_and_click_element(self.ELEMENTS_BUTTON, ErrMsg.elements_button_not_found)
        return ElementsPage(self.driver)
