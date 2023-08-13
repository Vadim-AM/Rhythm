"""Стандартный файл с фикстурами"""
from __future__ import annotations

from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from pages.main_page import MainPage


@pytest.fixture(params=["Chrome", "Firefox"])
def driver(request) -> Generator[WebDriver]:
    """
    Создаёт инстанс браузера с заданными параметрами
    --headless=new - headless режим браузера(в версии chrome 110+ необходим
    параметр 'new' для корректного определения дефолтной директории)
    Параметризована вызывается по разу за каждый переданный параметр"""
    browser = None
    if request.param == "Chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--headless=new")
        service = ChromeService(ChromeDriverManager().install())
        browser = webdriver.Chrome(service=service, options=options)
    elif request.param == "Firefox":
        options = webdriver.FirefoxOptions()
        options.add_argument("-headless")
        service = FirefoxService(GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service, options=options)
    browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()


@pytest.fixture
def main_page(driver) -> MainPage:
    """Opens a main page"""
    page = MainPage(driver)
    return page
