import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--brs_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: en or any other supported")

@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("brs_name")
    user_language = request.config.getoption("language")
    browser = None
    
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        #browser = webdriver.Chrome()
        
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        #browser = webdriver.Firefox()
        
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        
    else:
        raise pytest.UsageError("--brs_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()

#Есть одна важная особенность поведения конфигурационных файлов, о которой вы обязательно должны знать.
#PyTest автоматически находит и подгружает файлы conftest.py, которые находятся в директории с тестами. 
#Если вы храните все свои скрипты для курса в одной директории, будьте аккуратны и следите, чтобы не возникало ситуации, 
#когда вы запускаете тесты из папки tests:
#tests/
#├── conftest.py
#├── subfolder
#│   └── conftest.py
#│   └── test_abs.py
#следует избегать!
#В таком случае применяется ОБА файла conftest.py, что может вести к непредсказуемым ошибкам и конфликтам.
#selenium_course_solutions/
#├── section3
#│   └── conftest.py
#│   └── test_languages.py
#├── section4 
#│   └── conftest.py
#│   └── test_main_page.py
#правильно!

