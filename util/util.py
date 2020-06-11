from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class Util:
    driver: WebDriver = None

    def close_driver(self):
        """
        关闭 driver
        """
        sleep(2)
        self.driver.quit()

    def open_chrome_gui_browser(self):
        """
        打开 Chrome 浏览器
        """
        self.driver = webdriver.Chrome()

    def open_chrome_browser(self):
        """
        打开 Chrome headless 浏览器
        """
        chrome_options = Options()
        chrome_options.headless = True
        self.driver = webdriver.Chrome(options=chrome_options)

    def reuse_chrome(self, host: str = "localhost", port: str = "9222"):
        """
        复用已经打开的 Chrome
        """
        chrome_options = Options()
        chrome_options.add_experimental_option("debuggerAddress", (host + ":" + port))
        self.driver = webdriver.Chrome(options=chrome_options)

    def find(self, by, locator=""):
        """
        查找元素

        :param by: 定位方式
        :param locator: 定位符
        判断by是不是一个元祖，如果是则对元祖进行分拆
        """
        if isinstance(by, tuple):
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, locator)

    def get_title(self):
        """
        获取网页的标题
        :return: 网页标题
        """
        return self.driver.title
