from selenium.webdriver.common.by import By
from pages.hollder_driver import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WelcomPage(BasePage):
    def connect(self):
        self.driver.maximize_window()
        wait = WebDriverWait(self.driver, 10)
        connect_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[text()='התחברות']")))  
        #connect_button.click()
        self.driver.execute_script("arguments[0].click();", connect_button)      