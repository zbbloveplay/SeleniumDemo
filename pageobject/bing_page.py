from selenium.webdriver.common.by import By

from pageobject.base_page import BasePage


class BingPage(BasePage):
    _base_url = "https://cn.bing.com"

    # 输入关键字
    def input(self, kw: str):
        input_locator = (By.ID, "sb_form_q")
        self.util.find(input_locator).clear()
        self.util.find(input_locator).send_keys(kw)

    # 搜索
    def search(self):
        search_locator = (By.ID, "sb_form_go")
        self.util.find(search_locator).click()
