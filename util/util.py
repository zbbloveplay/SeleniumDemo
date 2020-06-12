from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains
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
        :return: 元素对象
        """
        if isinstance(by, tuple):
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by, locator)

    def click(self, by, locator=""):
        """
        点击元素

        :param by: 定位方式
        :param locator: 定位符
        """
        self.find(by, locator).click()

    def input(self, kw: str, by, locator=""):
        """
        输入字符串到元素

        :param kw: 输入字符
        :param by: 定位方式
        :param locator: 定位符
        """
        element = self.find(by, locator)
        element.clear()
        element.send_keys(kw)

    def move_to(self, by, locator=""):
        """
        模拟鼠标悬停在某个位置

        :param by: 定位方式
        :param locator: 定位符
        """
        element = self.find(by, locator)
        chain = ActionChains(self.driver)
        chain.move_to_element(element).perform()

    def get_title(self):
        """
        获取当前网页的标题

        :return: 网页标题
        """
        return self.driver.title

    def get_url(self):
        """
        获取当前网页的地址
        :return: URL
        """
        return self.driver.current_url

    def get_text(self, by, locator=""):
        """
        获取元素的文本

        :return: 元素文本
        """
        return self.find(by, locator).text

    def get_location(self, by, locator=""):
        """
        获取元素的位置

        :param by: 定位方式
        :param locator: 定位符
        """
        return self.find(by, locator).location

    def is_displayed(self, by, locator=""):
        """
        查看元素是否显现

        :param by: 定位方式
        :param locator: 定位符
        :return 元素是否显现（Ture/False）
        """
        return self.find(by, locator).is_displayed()

    def save_screenshot(self, path: str = 'screenshot.png'):
        """
        对网页进行截图

        :param path: 截图保存的路径
        """
        self.driver.save_screenshot(path)

    def max(self):
        """
        最大化浏览器
        """
        self.driver.maximize_window()

    def min(self):
        """
        最小化浏览器
        """
        self.driver.minimize_window()
