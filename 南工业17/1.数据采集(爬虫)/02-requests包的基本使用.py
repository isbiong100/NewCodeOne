import requests


# 1. 发送一个get请求并得到响应(response)
url = "https://www.baidu.com"
response = requests.get(url)

# 2. 验证是否成功 获取状态码
# print(response.status_code)

# # 3. 获取网页的内容(bytes字节型的)
# print(response.content)
# print(response.content.decode())

# 4. 获取网页的内容(str类型的)
# print(response.text)

# 5. 保存网络图片到本地
img_url = "http://a3.att.hudong.com/40/24/01300000241583122891242933732.jpg"
response = requests.get(img_url)

# 6. 获取图片的字节
img_content = response.content

# 7. 保存到本地
save_src = "./img/1.jpg"
with open(save_src, "wb") as f:
    # 开始写入文件
    f.write(img_content)
