# SeleniumDemo
使用PO模型编码，分层解耦。将底层方法、元素操作和业务逻辑分离。

技术选型：python + selenium + pytest + git + allure

- pageobject为页面类，封装元素操作
- testcase为测试用例类，实现业务逻辑
- util为工具类，封装底层方法

运行方法：
1. clone 到本地
2. 下载并配置 chromedriver 环境变量 
3. 开始测试 `pytest --alluredir=/tmp/my_allure_results`
4. 打开报告 `allure serve /tmp/my_allure_results`