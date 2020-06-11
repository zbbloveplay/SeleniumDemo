import allure

from pageobject.bing_page import BingPage


class TestBingSearch:
    def setup(self):
        self.bing = BingPage()

    def teardown(self):
        self.bing.util.close_driver()

    @allure.suite("必应搜索")
    def test_search(self):
        self.bing.input("hello")
        self.bing.search()
        assert "hello" in self.bing.util.get_title()
