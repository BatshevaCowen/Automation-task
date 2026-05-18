import pytest
from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.options import Options
load_dotenv()
@pytest.fixture
def driver(scope="function"):
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://entry-point.me")
    driver.implicitly_wait(10)
    yield driver
    driver.quit()









