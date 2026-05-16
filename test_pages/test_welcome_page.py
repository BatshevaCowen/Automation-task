from selenium import webdriver
from pages.welcome_page import Welcom
class TestPageWelcome:
    def test_open_page(self,driver):

        welcome = Welcom(driver)
        welcome.connect()
        url = driver.current_url
        exepted_url = "https://entry-point.me/login"
        assert url == exepted_url
        


    