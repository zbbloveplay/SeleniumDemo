from selenium.webdriver.common.by import By

from pageobject.base_page import BasePage


class BaiduPage(BasePage):
    _base_url = "https://www.baidu.com"

    # 输入关键字
    def input(self, kw: str):
        input_locator = (By.ID, "kw")
        self.find(input_locator).clear()
        self.find(input_locator).send_keys(kw)

    # 搜索
    def search(self):
        search_locator = (By.ID, "su")
        self.find(search_locator).click()

