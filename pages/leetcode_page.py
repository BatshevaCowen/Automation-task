from pages.hollder_driver import BaceHollderDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class PageLeetcode(BaceHollderDriver):
    def click_leetcode_buttom(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//span[text()='ליטקוד']").click()
        
    def solved_leetcode_count(self):
        return self.driver.find_element(By.XPATH, "//span[.='28 הושלמו']").text

