# SA STOCK  2019-11-17

import re
import requests
import traceback
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        # r.encoding = r.apparent_encoding 
        r.encoding = 'utf-8'
        return r.text
    except:
        return ""


def getStockList(lst, stockURL):
    print(stockURL)
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    currect_code = ''
    a = soup.find_all('a')  # 每个股票重复两次链接 跳过一次
    for i in a:
        try:
            # print(i.attrs)
            href = i.attrs['href']
            # print(href)
            # if re.findall(r"sh\d{6}", href)[0] is currect_code:
            #     continue
            # else:
            #     currect_code = re.findall(r"sh\d{6}", href)[0]
            lst.append(re.findall(r"sh\d{6}", href)[0])
            # print(lst)
            # continue
        except:
            continue
    # tr = soup.table.tr  #这样只能找到第一个
    key_list = ['code', 'name', 'latest', 'chg_pct', 'chg', 'colume', 'amount', 'open', 'hst_clost', 'low', 'high']
    trs = soup.table.find_all('tr')
    for tr in trs:
        a_trs = []
        a_trans = {}
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
        with open('SHANGHAI_trans.txt','a',encoding='utf-8') as ff:
            ff.write(str(a_trans)+'\n')
    print(len(lst))



def getStockInfo(lst, stockURL, tail, fpath):
    count = 0
    size = len(lst)
    for stock in lst:
        full_url = stockURL + stock + tail
        # print(full_url)
        html = getHTMLText(full_url)
        try:
            if html is "":
                continue
            infoDict = {}
            news = []
            boards = []
            soup = BeautifulSoup(html, 'html.parser')
            nameInfo = soup.find('table', attrs={'class': 'tabPic'})
            name = nameInfo.find_all(attrs={'class': 'Lfont'})[0]
            infoDict.update({'name': name.text})
            # <div id="info1_list_xw" style="display: block;">
            newsInfo = soup.find('div', attrs={'id': 'info1_list_xw'})
            newsSoups = newsInfo.find_all(attrs={'class': 'cDGray'})
            for new in newsSoups:
                a_new = {'time': '', 'title': ''}
                title = new.a.string
                time = new.span.string.replace('(', '').replace(')', '')
                a_new['time'] = time
                a_new['title'] = title
                news.append(a_new)
            infoDict['news'] = news

            boardInfo = soup.find('div', attrs={'id': 'info1_list_gg'})
            boardsSoup = boardInfo.find_all(attrs={'class': 'cDGray'})

            for board in boardsSoup:
                a_board = {'time': '', 'title': ''}
                title = board.a.string
                time = board.span.string.replace('(', '').replace(')', '')
                a_board['time'] = time
                a_board['title'] = title
                boards.append(a_board)
            infoDict['boards'] = boards

            # price = stockInfo.find_all(attrs={'id':'last'})[0]
            # infoDict['price']= price

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(infoDict) + '\n')
                count = count + 1
                print("\r当前进度 :{:.2f}% ".format(count * 100 / size, end=''))
        except:
            continue

if __name__ == "__main__":
    # stock_list_url = 'http://quote.eastmoney.com/center/gridlist.html#hk_stocks'
    stock_list_url = 'http://app.finance.ifeng.com/list/stock.php?t=ha&p='
    # stock_info_url = 'http://quote.eastmoney.com/hk/'
    stock_info_url = 'http://finance.ifeng.com/app/hq/stock/'
    tail = '/index.shtml'
    output_file = "SHANGHAI_stock.txt"
    slist = []
    # getStockList(slist, stock_list_url)

    for i in range(1,31):
        getStockList(slist,stock_list_url+str(i))
        print(' page ',i,' is OK')

    slist = list(set(slist))
    print('final',slist)
    getStockInfo(slist, stock_info_url, tail, output_file)
