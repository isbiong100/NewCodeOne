from selenium import webdriver


# 1. 创建webdriver对象
chrome_driver = webdriver.Chrome()

url = "https://search.jd.com/Search?keyword=%E6%80%A1%E5%AE%9D%E7%9F%BF%E6%B3%89%E6%B0%B4&enc=utf-8&spm=a.0.0&pvid=8ff9fafda3d64477a4826d1673eb0930"


# 1.1 设置窗口全屏
# chrome_driver.maximize_window()
# 查看无头浏览器对象提供的全部方法
# print(dir(chrome_driver))

# 2. 尝试打开一个网址
chrome_driver.get(url)

# 3. 执行js脚本
chrome_driver.execute_script(
    'window.scrollTo(0, document.body.scrollHeight);'
)