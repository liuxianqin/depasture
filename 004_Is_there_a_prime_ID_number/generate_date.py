import re

rex = r"(15|16|17|18|19|([23456789]\d))\d{2}((0[1-9])|(10|11|12))(([0-2][1-9])|10|20|30|31)"

with open('date.txt','w') as f:
    for i in range(18800101,20201231):
        istr = str(i)
        print(istr)
        if re.match(rex,istr):
            f.write(istr+"\n")
            print("***OK***",istr)
