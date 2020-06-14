import requests


# 请求热门电视剧
url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"
# 请求标签
url2 = "https://movie.douban.com/j/search_tags?type=tv&source="

request_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/79.0.3945.88 Safari/537.36"
}

# 1. 发送请求
response = requests.get(url=url2, headers=request_header)

# 2. 输出
# print(response.status_code)
# print(response.content.decode())

res = response.content.decode()

# 3. 查看类型 json其实是字符串格式
print(res)
print(type(res))
print('-' * 10)

# python类型的字典
d = {"name": "张三", "age": 18}
print(d)
print(type(d))


# 服务器反爬虫常用手法:
# 1. 验证码/滑块
# 2. 加密
# 3. ip地址

# 针对3:
# 1. 使用代理
# 2. 使用代理池
# 3. 伪装身份 user-agent




