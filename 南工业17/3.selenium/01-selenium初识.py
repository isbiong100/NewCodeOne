from selenium import webdriver


# 1. 创建webdriver对象
chrome_driver = webdriver.Chrome()

# 1.1 设置窗口全屏
# chrome_driver.maximize_window()
# 查看无头浏览器对象提供的全部方法
# print(dir(chrome_driver))

# 2. 尝试打开一个网址
chrome_driver.get("http://www.baidu.com")

# 显示网页源码
# print(chrome_driver.page_source)
# chrome_driver.get_cookie()   获取当前cookie
# chrome_driver.current_url    获取当前浏览的url地址
# chrome_driver.close()        关闭窗口

# 获取页面内容
# r = chrome_driver.find_element_by_xpath("/html/head/title").text
# print(r)
# print(type(r))
# print(chrome_driver.title)

# 查找当前页面中的输入框
# chrome_driver.find_element_by_xpath('//*[@id="kw"]').send_keys("python")
chrome_driver.find_element_by_name("wd").send_keys("python")

# 点击按钮来完成搜索
chrome_driver.find_element_by_xpath('//*[@id="su"]').click()



# 关闭窗口
# chrome_driver.close()

