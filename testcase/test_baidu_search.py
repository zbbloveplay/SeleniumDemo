from pageobject.baidu_page import BaiduPage
import allure

class TestBaiduSearch:
    def setup(self):
        self.baidu = BaiduPage()

    def teardown(self):
        self.baidu.close()

    @allure.suite("百度搜索")
    def test_search(self):
        self.baidu.input("hello")
        self.baidu.search()