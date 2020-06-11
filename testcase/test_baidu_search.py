import allure

from pageobject.baidu_page import BaiduPage


class TestBaiduSearch:
    def setup(self):
        self.baidu = BaiduPage()

    def teardown(self):
        self.baidu.util.close_driver()

    @allure.suite("百度搜索")
    def test_search(self):
        self.baidu.input("hello")
        self.baidu.search()
        assert "hello" in self.baidu.util.get_title()
