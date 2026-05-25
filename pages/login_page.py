from pages.hollder_driver import BasePage
from selenium.webdriver.common.by import By
import os

class PageLogin(BasePage):
    def click_log_in(self):
        self.driver.implicitly_wait(10)
        email_user = self.driver.find_element(By.ID, "login-email")
        password_user = self.driver.find_element(By.ID, "login-password")
        email_user.send_keys(os.getenv("ENTRYPOINT_USERNAME"))
        password_user.send_keys(os.getenv("ENTRYPOINT_PASSWORD"))
        login_btn = self.driver.find_element(By.XPATH, "//span[text()='כניסה']")
        self.driver.execute_script("arguments[0].click();", login_btn)
        
    