import re
from bs4 import BeautifulSoup

# <th><a href="?t=ha&f=symbol&o=asc&p=1">代码</a></th>
#     <th><a href="?t=ha&f=name&o=asc&p=1">名称</a></th>
#     <th><a href="?t=ha&f=last&o=asc&p=1">最新价</a></th>
#     <th><a href="?t=ha&f=chg_pct&o=asc&p=1">涨跌幅&darr;</a></th>
#     <th><a href="?t=ha&f=chg&o=asc&p=1">涨跌额</a></th>
#     <th><a href="?t=ha&f=volume&o=asc&p=1">成交量</a></th>
#     <th><a href="?t=ha&f=amount&o=asc&p=1">成交额</a></th>
#     <th><a href="?t=ha&f=open&o=asc&p=1">今开盘</a></th>
#     <th><a href="?t=ha&f=hst_close&o=asc&p=1">昨收盘</a></th>
#     <th><a href="?t=ha&f=low&o=asc&p=1">最低价</a></th>
#     <th><a href="?t=ha&f=high&o=asc&p=1">最高价</a></th>

transes = []
key_list = ['code','name','latest','chg_pct','chg','colume','amount','open','hst_clost','low','high']
# a_trans = {'code':'','name':'','latest':'','chg_pct':'','chg':'','colume':'','amount':'','open':'','hst_clost':'','low':'','high':''}
# a_trs = []
with open('testSHANGHAIfile.html','r') as f :
    text = f.read()
soup = BeautifulSoup(text,'html.parser')
# tr = soup.table.tr  #这样只能找到第一个
trs = soup.table.find_all('tr')
for tr in trs:
    a_trs = []
    a_trans ={}
    tds = tr.find_all('td')
    for td in tds:
        # print(td.string)
        a_trs.append(td.string)
    # print(a_trs)
    # print(len(key_list))
    # print(len(a_trs))
    if len(key_list) == len(a_trs):
        for i in range((len(key_list))):
            a_trans[key_list[i]] = a_trs[i]
    print(a_trans)
