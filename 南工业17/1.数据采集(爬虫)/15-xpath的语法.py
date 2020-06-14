from lxml import etree
import re


html = """
    <div>
        <ul>
            <li class='i1'><a href='link1.html'>c语言</a></li>
            <li class='i2'><a href='link2.html'>c++</a></li>
            <li class='i3'><a href='link3.html'>python</a></li>
            <li class='i4'><a href='link4.html'>mongodb</a></li>
            <li class='i5'><a href='link5.html'>mysql</a></li>
            <li class='i6'><a href='link6.html'>lua</a></li>       
        </ul>
    </div>

    <div class='neuedu'>
        <ul>
            <li class='i1'><a href='link1.html'>aa</a></li>
            <li class='i2'><a href='link2.html'>bb</a></li>
            <li class='i3'><a href='link3.html'>cc</a></li>
            <li class='i4'><a href='link4.html'>dd</a></li>
            <li class='i5'><a href='link5.html'>ee</a></li>
            <li class='i6'><a href='link6.html'>ff</a></li>       
        </ul>

        <ul>
            <li class='i1'><a href='link1.html'>连城诀</a></li>
            <li class='i2'><a href='link2.html'>射雕英雄</a></li>
            <li class='i3'><a href='link3.html'>倚天屠龙</a></li>
            <li class='i4'><a href='link4.html'>笑傲江湖</a></li>
            <li class='i5'><a href='link5.html'>鹿鼎记</a></li>
            <li class='i6'><a href='link6.html'>大唐双龙</a></li>       
        </ul>
    </div>

"""

# 1. 正则
# print(re.compile("<ul>.*?<li class='i1'>.*?>(.*?)<", re.S).findall(html))

# 1. 使用xpath
# 1.1 先创建对象
tree_object = etree.HTML(html)
# 1.2 使用上面的对象利用xpath语法来进行提取数据了

# --------- 获取class为i1的li标签下的a标签中的内容
# results = tree_object.xpath('//li[@class="i1"]/a/text()')
# results = tree_object.xpath("//div/ul/li[@class='i1']/a/text()")
# results = tree_object.xpath("//a[@href='link1.html']/text()")

# --------- 获取属性值
# results = tree_object.xpath('//ul/li/a/@href')

# 获取属性为neuedu标签下的第一个ul标签下的a标签的内容
# results = tree_object.xpath('//div[@class="neuedu"]/ul[1]/li/a/text()')
# results = tree_object.xpath('//div[@class="neuedu"]/ul[last()-1]/li/a/text()')
# results = tree_object.xpath('//div[@class="neuedu"]/ul[last()-1]//a/text()')

# *表示不限定节点
# results = tree_object.xpath('//*[@class="neuedu"]//a/text()')

# position()
# results = tree_object.xpath('//*[@class="neuedu"]/ul[1]//a/text()')
# print(results)
