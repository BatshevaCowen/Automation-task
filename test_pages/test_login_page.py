from pages.login_page import PageLogin 
from pages.welcome_page import Welcom
class TestPageLogin:
    def test_open_page_login(self,driver):
        welcome = Welcom(driver)
        welcome.connect()
        log_in = PageLogin(driver)
        log_in.click_log_in()
        
        url = driver.current_url
        exepted_url = "https://entry-point.me/dashboard"
        assert url == exepted_url

        


