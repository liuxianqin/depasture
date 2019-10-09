#coding=utf-8

from  datetime import datetime,timedelta
import time

class countDate:
    def __init__(self,filename):
        self.filename = filename
        self.readfile()

    def givedate(self,day):

        countsec = day * 86400

        x_0 = -62135625943 + countsec

        x_1 = datetime(1970, 1, 1) + timedelta(seconds=x_0)

        x_2 = x_1.strftime("%Y-%m-%d")
        print(x_2)
        return x_2

    def readfile(self):
        days = []
        rows = 0
        with open(self.filename, 'r') as f:
            lines = f.readlines()
            rows = len(lines)
            print("行数", len(lines))
            for line in lines:
                line = line.strip('\n')
                print(line)
                # odom = line.split(',')
                # a = map(float, odom)
                days.append(int(line))
        dates = []
        for day in days:
            thedate = self.givedate(day)
            dates.append(thedate)
        with open(self.filename,'w') as wf:
            for i in range(rows):
                wf.write(str(days[i])+"\t"+ str(dates[i])+ "\n" )





if __name__=="__main__":

    filename = "days2date.txt"
    a = countDate(filename)



