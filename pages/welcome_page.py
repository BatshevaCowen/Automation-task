from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from pages.hollder_driver import BaceHollderDriver

class Welcom(BaceHollderDriver):
    def connect(self):
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//span[text()='התחברות']").click()