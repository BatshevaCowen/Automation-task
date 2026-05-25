from pages.leetcode_page import PageLeetcode
from pages.welcome_page import Welcom
from pages.login_page import PageLogin

class TestLeetcode:
    def test_open_page_leetcode(self,driver):
        welcome = Welcom(driver)
        welcome.connect()
        log_in = PageLogin(driver)
        log_in.click_log_in()
        leetcode_click = PageLeetcode(driver)
        leetcode_click.click_leetcode_buttom()

        url = driver.current_url
        exepted_url = "https://entry-point.me/dashboard/leetcode"
        assert url == exepted_url

#כתבי טסט בפייתון שנכנס לאתר בשם המלווה ובודק כמה שאלות ליטקוד הוא עשה שהוגש וקיבל משוב
    def test_solved_leetcode_count(self,driver):
        welcome = Welcom(driver)
        welcome.connect()
        log_in = PageLogin(driver)
        log_in.click_log_in()
        leetcode_click = PageLeetcode(driver)
        leetcode_click.click_leetcode_buttom()
        solved_leetcode_count = (leetcode_click.solved_leetcode_count())
        solved_leetcode_count = int(solved_leetcode_count.split()[0])
        assert solved_leetcode_count >= 6, f"Expected at least 6 solved leetcode items, got {solved_leetcode_count}"
        #assert text_element > 5
    