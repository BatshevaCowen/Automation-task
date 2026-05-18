from pages.login_page import PageLogin 
from pages.welcome_page import Welcom
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class TestPageLogin:
    def test_open_page_login(self,driver):
        welcome = Welcom(driver)
        welcome.connect()
        log_in = PageLogin(driver)
        log_in.click_log_in()
        WebDriverWait(driver, 10).until(EC.url_contains("dashboard"))
        url = driver.current_url
        exepted_url = "https://entry-point.me/dashboard"
        assert url == exepted_url

        


