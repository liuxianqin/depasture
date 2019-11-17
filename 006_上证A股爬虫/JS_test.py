import requests
#检测是否有动态页面


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


if __name__ == "__main__":
    url1 = 'http://quote.eastmoney.com/center/gridlist.html#hk_stocks'
    url2 = 'http://quote.eastmoney.com/hk/00886.html'
    url3 = 'http://app.finance.ifeng.com/list/stock.php'
    url4 = 'http://finance.ifeng.com/app/hq/stock/sh600592/index.shtml'
    text = getHTMLText(url4)
    with open('testfile.html','w') as f:
        f.write(text)
