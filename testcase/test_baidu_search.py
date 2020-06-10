from pageobject.baidu_page import BaiduPage


class TestBaiduSearch:
    def setup(self):
        self.baidu = BaiduPage()

    def teardown(self):
        self.baidu.close()

    def test_search(self):
        self.baidu.input("hello")
        self.baidu.search()