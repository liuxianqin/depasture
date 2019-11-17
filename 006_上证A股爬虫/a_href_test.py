import re

astr = "http://finance.ifeng.com/app/hq/stock/sh600358/index.shtml"
num = re.findall(r"sh\d{6}", astr)
print(num)