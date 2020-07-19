from time import sleep

import allure
import pytest

from pageobject.baidu_page import BaiduPage
from pageobject.base_page import BasePage


class TestBaiduSearch:
    data = BasePage.util.load_yaml("data/baidu_search.data.yaml")

    def setup(self):
        self.baidu = BaiduPage()
        
    def teardown(self):
        self.baidu.util.close_driver()

    @allure.suite("百度搜索")
    @allure.title('{title}')
    @pytest.mark.parametrize("kw, title", data["test_search"])
    def test_search(self, kw, title):
        self.baidu.input(kw)
        self.baidu.search()
        # TODO 点击搜索后，网页标题不会马上改变，需要等待请求返回
        # NOTE 各个搜索引擎都会对字符进行“规范化”，比如去掉变音符号
        # NOTE 颜文字中的一些字符会发生转换，例如「(*´▽｀)ノノ」转换成「(*´▽`)ノノ」
        # NOTE ChromeDriver only supports characters in the BMP，所以不能搜索传递 emoji。
        #       如果硬要传，可以通过JS添加字符串到元素里：https://stackoverflow.com/a/61043442
        sleep(2)
        assert kw in self.baidu.util.get_title()
