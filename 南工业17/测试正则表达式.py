import re


html = """
<table width="100%" border="0" cellspacing="0" cellpadding="0" class="tbspan" style="margin-top:6px">
    <tr>
        <td height="1" colspan="2" background="/templets/img/dot_hor.gif"></td>
    </tr>
    <tr>
        <td width="5%" height="26" align="center"><img src="/templets/img/item.gif" width="18" height="17"></td>
        <td height="26">
            <b>
                <a href="/i/101796.html" class="ulink" title="2019年美国6.5分动作科幻片《星球大战9：天行者崛起》BD双字">2019年美国6.5分动作科幻片《星球大战9：天行者崛起》BD双字</a>
            </b>
        </td>
    </tr>
    
</table>
<table width="100%" border="0" cellspacing="0" cellpadding="0" class="tbspan" style="margin-top:6px">
    <tr>
        <td height="1" colspan="2" background="/templets/img/dot_hor.gif"></td>
    </tr>
    <tr>
        <td width="5%" height="26" align="center"><img src="/templets/img/item.gif" width="18" height="17"></td>
        <td height="26">
            <b>
                <a href="/i/101798.html" class="ulink" title="2020年欧美7.7分犯罪剧情片《逃离比勒陀利亚》BD中英双字">2020年欧美7.7分犯罪剧情片《逃离比勒陀利亚》BD中英双字</a>
            </b>
        </td>
    </tr>
</table>
"""

result_list = re.compile('<table width="100%".*?<td height="26">.*?<a href="(.*?)".*?title="(.*?)">', re.S).findall(html)
print(result_list)