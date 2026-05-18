from pages.hollder_driver import BaceHollderDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import os
from dotenv import load_dotenv

class PageLogin(BaceHollderDriver):
    def click_log_in(self):
        self.driver.implicitly_wait(10)
        email_user = self.driver.find_element(By.ID, "login-email")
        password_user = self.driver.find_element(By.ID, "login-password")
        email_user.send_keys(os.getenv("ENTRYPOINT_USERNAME"))
        password_user.send_keys(os.getenv("ENTRYPOINT_PASSWORD"))
        self.driver.find_element(By.XPATH, "//span[text()='כניסה']").click()
        
    