import re


# 需要检测的文本
# content = 'Hello 123 4567 World_This is a Regex Demo, Regex'
# #
# # # 1. 匹配字符串Hello 123 4567 World_This
# pattern = '^Hello\s\d\d\d\s\d{4}\s\w{10}'
#
# # 2. 匹配任意字符
# # pattern = '.*'
# # pattern = '.+'
#
# # 3. 匹配整个字符串
# # pattern = 'He.*?(\d+).*Demo'
#
# # 4.
# pattern = 'Wo.*?'
#
# # 匹配返回的结果
# # match() 从字符串起始位置匹配正则表达式
# res = re.match(pattern, content)
# print(res.group())

# print(res.group())


# 贪婪模式和非贪婪模式
html = """
    <html>
        <div class="book">
            <book><p>c语言1</p></book>
            <book><p>c语言2</p></book>
            <book><p>c语言3</p></book>
        </div>
        <div>
            <book>
                <p>python程序设计</p>
            </book>
        </div>
    </html>
"""
# html = """
#     <html>
#         <div class="book">
#             <book>
#                 <p>c语言1</p>
#             </book>
#             <book><p>c语言2</p></book>
#             <book><p>c语言3</p></book>
#         </div>
#     </html>
# """

# 1. 使用贪婪模式
# result1 = re.compile('<div>.*?<book>.*<p>.*</p>', re.S).findall(html)
# print("------ 使用贪婪模式匹配结果 ------- 尽可能多的去匹配")
# print(result1)
#
# # 2. 使用非贪婪
# result2 = re.compile('<div>.*?<book>.*?<p>.*?</p>', re.S).findall(html)
# print("------ 使用非贪婪模式匹配结果 ------- 尽可能少的去匹配")
# print(result2)


# 3. 提取书名
# result = re.compile('<p>(.*?)</p>', re.S).findall(html)
# # result = re.compile('<book><p>(.*?)</p>', re.S).findall(html)
# print(result)


# ------------------------- 练习
# s = "AX B C D"
# #
# # # 1. 提取结果是A B和C D 规则怎么写
# r1 = re.compile('\w+\s\w').findall(s)
# print(type(r1))

# 2. 提取结果是A 和C 提取规则怎么写?
# r2 = re.compile('(\w+)\s+\w+').findall(s)
# print(r2)
#
# # 3. 提取结果是(A,B)和(C,D) 提取规则又怎么写?
# r3 = re.compile('(\w+)\s(\w+)').findall(s)
# print(r3)


html = '''
<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">经典老歌列表</p>
<ul id="list" class="list-group">
<li data-view="2"><a href="/1.mp3" singer="吴奇隆">一路上有你</a></li>
<li data-view="7"><a href="/2.mp3" singer="任贤齐">沧海一声笑</a></li>
<li data-view="4"><a href="/3.mp3" singer="齐秦">往事随风</a></li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5"><a href="/6.mp3" singer="邓丽君">但愿人长久</a></li>
</ul>
</div>'''


# result = re.search('<li.*?singer="(.*?)">(.*?)</a>', html, re.S)
# print(result.group())
# print(type(result.group()))


# result = re.compile('<li.*?singer="(.*?)">(.*?)</a>', re.S).findall(html)
# print(result[0][0])
# print(type(result))


# html2 = '<li data-view="4" class="active"><a href="/3.mp3" singer="齐秦">往事随风</a></li>'
# result = re.search('li.*?active.*?singer="(.*?)">(.*?)<', html2, re.S)
# print(result.group(0))
# print(result.group(1))
# print(result.group(2))

# li data-view="4" class="active"><a href="/3.mp3" singer="齐秦">往事随风<









