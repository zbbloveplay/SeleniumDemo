import allure

from pageobject.bing_page import BingPage


class TestBingSearch:
    def setup(self):
        self.bing = BingPage()

    def teardown(self):
        self.bing.close()

    @allure.suite("必应搜索")
    def test_search(self):
        self.bing.input("hello")
        self.bing.search()