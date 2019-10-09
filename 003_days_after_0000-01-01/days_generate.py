import random

filename = "days2date.txt"

with open(filename,'w') as f:
    for i in range(200):
        days = random.randint(1,365*23*100)
        print(days)
        f.write( str(days)+"\n" )