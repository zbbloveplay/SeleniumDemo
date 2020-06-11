from selenium.webdriver.remote.webdriver import WebDriver

from util.util import Util


class BasePage:
    _base_url = ""
    util = Util()

    def __init__(self, driver: WebDriver = None, reuse=False):
        if driver is None:
            if reuse:
                self.util.reuse_chrome()
            else:
                self.util.open_chrome_gui_browser()
            self.util.driver.implicitly_wait(5)
        else:
            self.util.driver = driver

        if self._base_url != "":
            self.util.driver.get(self._base_url)
