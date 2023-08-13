## Rhythm

#### Скопировать [проект](https://github.com/Vadim-AM/Rhythm.git) себе на локальную машину и последовательно выполнить следующие команды в консоли:
    >>>> pip install --upgrade pip
    >>>> pip install -r requirements.txt
    >>>> pytest

#### *Перед выполнением убедитесь, что на вашем компьютере установлены и обновлены последние версии браузеров Chrome и Firefox*

#### Тесты будут запущены в 2 потока в headless режиме. Для отображения графического интерфейса браузеров необходимо закомментировать или удалить строки в файле conftest.py:
        options.add_argument("--headless=new")  Для браузера Chrome
        options.add_argument("-headless") Для браузера Firefox


