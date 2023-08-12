"""Содержит тесты страницы checkbox"""
from pages.check_box_page import CheckBoxPage
from pages.main_page import MainPage
from src.texts import Texts, ErrMsg


class TestCheckBox:
    """Содержит тесты чекбоксов"""

    def test_the_word_file_check_box(self, main_page: MainPage):
        """ #номер кейса: Проверка хинта при выборе чекбокса Word File"""
        main_page.open_an_elements_page() \
            .open_check_box_page() \
            .expand_home_dir() \
            .expand_downloads_dir() \
            .check_the_word_file_box()
        hint_text = main_page.get_text(CheckBoxPage.RESULT_HINT)
        assert hint_text == Texts.result_hint
