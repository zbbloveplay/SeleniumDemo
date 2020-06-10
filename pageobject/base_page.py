from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver

# TODO 将以下方法封装到util类
class BasePage:
    _base_url = ""
    _driver = None

    # 初始化driver
    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse:
                chrome_options = Options()
                chrome_options.add_experimental_option("debuggerAddress", "localhost:9222")
                self._driver = webdriver.Chrome(options=chrome_options)
            else:
                self._driver = webdriver.Chrome()
            self._driver.implicitly_wait(5)
        else:
            self._driver = driver

        if self._base_url != "":
            self._driver.get(self._base_url)

    # 关闭driver
    def close(self):
        sleep(10)
        self._driver.quit()

    # 查找元素
    def find(self, by, locator=""):
        if isinstance(by, tuple):  # 判断by是不是一个元祖，如果是则对元祖进行分拆
            return self._driver.find_element(*by)
        else:
            return self._driver.find_element(by, locator)

    # 获取driver
    def get_driver(self):
        return self._driver

    # 打开浏览器，使用headless模式
    def open_browser(self):
        pass

    # 打开浏览器，使用GUI模式
    def open_gui_browser(self):
        pass

    # 关闭浏览器
    def close_browser(self):
        pass

    # 浏览器最大化
    def max_browser(self):
        pass

