"""Стандартный файл с фикстурами"""
from __future__ import annotations

import os
import shutil
from typing import Generator

import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from config import Hosts
from pages.main_page import MainPage


@pytest.fixture
def driver(request) -> Generator[WebDriver]:
    """
    Создаёт инстанс браузера с заданными параметрами
    --headless=new - headless режим браузера(в версии chrome 110+ необходим
    параметр 'new' для корректного определения дефолтной директории)
    --no-sandbox - Добавляется только в том случае,
    если установлена системная переменная окружения CI,
     если пользователь в системе Linux не установлен, или при выполнении внутри контейнера Docker.
    Отключает песочницу для всех типов процессов, которые обычно находятся в песочнице.
    Используется только в качестве переключателя на уровне браузера в целях тестирования.
    --disable-dev-shm-usage - Добавляется только при установленной переменной
    системного окружения CI или внутри экземпляра docker.
    Раздел /dev/shm слишком мал в некоторых средах виртуальных машин,
    что приводит к сбою или отказу Chrome"""
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless=new")
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-dev-shm-usage")
    service = ChromeService(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service, options=options)
    browser.set_window_size(1920, 1080)
    yield browser
    browser.quit()


@pytest.fixture
def main_page(driver) -> MainPage:
    """Opens a main page"""
    page = MainPage(driver)
    page.open()
    return page
