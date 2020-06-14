import requests
import json


# 1. 请求的地址
url = "https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=10&page_start=0"
# 2. 构造请求头
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
}
# 3. 发送请求获取响应(数据)
res = requests.get(url=url, headers=header).content.decode()

# print(res)
# print(type(res))

# json.loads 将带有字典格式的字符串(json字符串)转换成python对象
res_dict = json.loads(res)

# 在列表中遍历
# print(len(res_dict["subjects"]))
# for tv_info in res_dict["subjects"]:
#     print(tv_info["title"])
#     print(tv_info["rate"])
#     print("-" * 50)


# 关于写入文件
# with open("./db_tv_new_3.json", "w", encoding="utf-8") as f:
#     # 1.1 直接写入得到的字符串
#     # f.write(res)
#
#     # 1.2 使用json.dumps()
#     # f.write(json.dumps(res_dict, ensure_ascii=False, indent=4))
#
#     # 1.3 把python类型
#     json.dump(res_dict, f, ensure_ascii=False, indent=4)


# 关于读取文件
with open("./db_tv_new.json", "r", encoding="utf-8") as f:
    # 1.1 直接读取文件中的内容
    ret = f.read()
    # print(ret)
    # print(type(ret))

    # 1.2
    r = json.loads(ret)
    print(r)
    print(type(r))

