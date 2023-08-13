"""Содержит класс страницы Elements"""
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.check_box_page import CheckBoxPage
from src.texts import ErrMsg


class ElementsPage(BasePage):
    """Содержит локаторы и методы страницы Elements"""

    CHECK_BOX_BUTTON = (By.XPATH, "//li/span[text()='Check Box']")

    def open_check_box_page(self) -> CheckBoxPage:
        """Открывает страницу Check Box"""
        self.find_and_click_element(self.CHECK_BOX_BUTTON, ErrMsg.check_box_button_not_found)
        return CheckBoxPage(self.driver)
