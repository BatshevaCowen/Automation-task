from pages.leetcode_page import PageLeetcode


class TestLeetcode:
    def test_open_page_leetcode(self, authenticated_driver):
        leetcode_click = PageLeetcode(authenticated_driver)
        leetcode_click.click_leetcode_buttom()
        url = authenticated_driver.current_url
        exepted_url = "https://entry-point.me/dashboard/leetcode"
        assert url == exepted_url

    # כתבי טסט בפייתון שנכנס לאתר בשם המלווה ובודק כמה שאלות ליטקוד הוא עשה שהוגש וקיבל משוב
    def test_solved_leetcode_count(self, authenticated_driver):
        leetcode_click = PageLeetcode(authenticated_driver)
        leetcode_click.click_leetcode_buttom()
        solved_leetcode_count = leetcode_click.solved_leetcode_count()
        solved_leetcode_count = int(solved_leetcode_count.split()[0])
        assert solved_leetcode_count >= 6, (
            f"Expected at least 6 solved leetcode items, got {solved_leetcode_count}"
        )
