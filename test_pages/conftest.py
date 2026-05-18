import pytest
from selenium import webdriver
import os
from dotenv import load_dotenv
load_dotenv()
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://entry-point.me")
    yield driver
    driver.quit()









