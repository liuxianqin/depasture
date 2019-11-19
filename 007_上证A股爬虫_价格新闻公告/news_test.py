import traceback
from bs4 import BeautifulSoup


def getStockInfo():
    with open('testfile.html', 'r') as f:
        html = f.read()

    try:
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


    except:
        traceback.print_exc()


getStockInfo()
