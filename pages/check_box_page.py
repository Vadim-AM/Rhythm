"""Содержит класс страницы checkbox"""
from __future__ import annotations

from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from src.texts import ErrMsg


class CheckBoxPage(BasePage):
    """Содержит локаторы и методы страницы checkbox"""
    HOME_CHEVRON = (By.XPATH, "//span[text()='Home']/../../button")
    DOWNLOADS_CHEVRON = (By.XPATH, "//span[text()='Downloads']/../../button")
    WORD_DOCK_CHECK_BOX = (By.XPATH, "//span[text()='Word File.doc']/../span[contains(@class, 'checkbox')]")
    RESULT_HINT = (By.XPATH, "//div[@id='result']")

    def expand_home_dir(self) -> CheckBoxPage:
        """Нажимает на шеврон Home, раскрывает директорию"""
        self.find_and_click_element(self.HOME_CHEVRON, ErrMsg.chevron_home_not_found)
        return self

    def expand_downloads_dir(self) -> CheckBoxPage:
        """Нажимает на шеврон Downloads, раскрывает директорию"""
        self.find_and_click_element(self.DOWNLOADS_CHEVRON, ErrMsg.chevron_home_not_found)
        return self

    def check_the_word_file_box(self) -> CheckBoxPage:
        """Нажимает чекбокс Word File.doc"""
        self.find_and_click_element(self.WORD_DOCK_CHECK_BOX, ErrMsg.check_box_word_not_found)
        return self
