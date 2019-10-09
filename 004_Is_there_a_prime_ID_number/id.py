import math

l=[2,3]
f=open('id.txt','a')
for i in range(5,99999999999):
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            break
    else:
        f.write(str(i)+" ")
f.close()
print(" ".join(map(str,l)))
