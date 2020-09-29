import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(
            executable_path="/Users/nagarajualapati/PycharmProjects/Google_Pytest_e2e/driver/chromedriver")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(
            executable_path="/Users/nagarajualapati/PycharmProjects/Google_Pytest_e2e/driver/geckodriver")
    elif browser_name == "edge":
        driver = webdriver.Ie(
            executable_path="/Users/nagarajualapati/PycharmProjects/Google_Pytest_e2e/driver/msedgedriver")
    driver.get("https://www.google.com/intl/en_in/drive/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()