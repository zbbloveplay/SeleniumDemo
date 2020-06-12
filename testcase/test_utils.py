import logging

from selenium.webdriver.common.by import By

from pageobject.baidu_page import BaiduPage


class TestUtils:
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMAT)  # 默认只有WARNING级别及以上的日志才会被输出

    def setup(self):
        self.baidu = BaiduPage()

    def teardown(self):
        self.baidu.util.close_driver()

    def test_max_window(self):
        self.baidu.util.max()

    def test_min_window(self):
        self.baidu.util.min()

    def test_save_screenshot(self):
        self.baidu.util.max()
        self.baidu.util.save_screenshot()

    def test_get_url(self):
        url = self.baidu.util.get_url()
        logging.info(url)
        assert "baidu.com" in url

    def test_get_location(self):
        location = self.baidu.util.get_location(By.ID, "kw")
        logging.info(location)

    def test_move_to(self):
        """
        测试移动到元素上，对应的隐藏的元素是否会显现
        """
        assert False is self.baidu.util.is_displayed(By.CLASS_NAME, "voice-hover")
        self.baidu.util.move_to(By.CLASS_NAME, "ipt_rec")
        assert True is self.baidu.util.is_displayed(By.CLASS_NAME, "voice-hover")

