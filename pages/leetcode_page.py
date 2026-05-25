from pages.hollder_driver import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageLeetcode(BasePage):
    def click_leetcode_buttom(self):
        self.driver.implicitly_wait(10)
        leetcode_btn = self.driver.find_element(By.XPATH, "//span[text()='ליטקוד']")
        self.driver.execute_script("arguments[0].click();", leetcode_btn)
        
    def solved_leetcode_count(self):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.XPATH,"//span[.='33 הושלמו']")))
        return element.text
    

