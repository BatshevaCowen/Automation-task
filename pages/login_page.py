from pages.hollder_driver import BaceHollderDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class PageLogin(BaceHollderDriver):
    def click_log_in(self):
        self.driver.implicitly_wait(10)
        email_user = self.driver.find_element(By.ID, "login-email")
        password_user = self.driver.find_element(By.ID, "login-password")
        email_user.send_keys("bat7cn@gmail.com")
        password_user.send_keys("Bat71234")
        self.driver.find_element(By.XPATH, "//span[text()='כניסה']").click()
    