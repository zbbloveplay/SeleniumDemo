from pageobject.bing_page import BingPage


class TestBingSearch:
    def setup(self):
        self.bing = BingPage()

    def teardown(self):
        self.bing.close()

    def test_search(self):
        self.bing.input("hello")
        self.bing.search()