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
    html = getHTMLText(stockURL)
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')  # 每个股票重复两次链接 跳过一次
    for i in a:
        try:
            print(i.attrs)
            href = i.attrs['href']
            print(href)
            lst.append(re.findall(r"sh\d{6}", href)[0])
            print(lst)
            continue
        except:
            continue


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
    stock_list_url = 'http://app.finance.ifeng.com/list/stock.php?t=ha'
    # stock_info_url = 'http://quote.eastmoney.com/hk/'
    stock_info_url = 'http://finance.ifeng.com/app/hq/stock/'
    tail = '/index.shtml'
    output_file = "HA_stock.txt"
    slist = []
    getStockList(slist, stock_list_url)
    print(slist)
    getStockInfo(slist, stock_info_url, tail, output_file)
