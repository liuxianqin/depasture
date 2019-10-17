import random

order_list = [ '00'+str(i) for i in range(10) ]
order_list += [  '0'+str(i) for i in range(10,100)]
order_list += [str(i) for i in range(100,1000)]
# print(order_list)
doublelist = ['0','2','4','6','8']
lines = []
result = []



def rabinMiller(num):
    # 快速幂
    s = num - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1

    # 最小费马定理
    for trials in range(5):
        a = random.randrange(2, num - 1)
        v = pow(a, s, num)
        if v != 1:
            i = 0
            while v != (num - 1):
                if i == t - 1:
                    return False
                else:
                    i = i + 1
                    v = (v ** 2) % num
    return True


def isPrime(num):
    if num < 2:
        return False
    # prime.txt是存放素数表的文件
    # lowPrimes = open('prime.txt', 'r')
    lowPrimes = [2,3,5,7,11,13,17,19]
    if num in lowPrimes:
        return True
    for prime in lowPrimes:
        if num % prime == 0:
            return False
    return rabinMiller(num)


# generateLargePrime函数返回素数。它选出一个大的随机数保存到num
# 再将num传到isPrime和rabinMiller进行判断是不是素数
# 先isPrime后rabinMiller是因为复杂度先简后繁
def generateLargePrime(keysize=1024):
    while True:
        num = random.randrange(2 ** (keysize - 1), 2 ** keysize)
        if isPrime(num):
            return num

def get_check_digit(idstr):
    """通过身份证号获取校验码"""
    check_sum = 0
    for i in range(0, 17):
        check_sum += ((1 << (17 - i)) % 11) * int(idstr[i])
    check_digit = (12 - (check_sum % 11)) % 11
    return str(check_digit)

with open('date.txt','r') as f:
    lines = f.readlines()
    print(len(lines))


print(len(lines))

with open('result_full.txt','w') as fw:
    for line in lines[:10]:
        datestr = line.strip('\n')
        dateint = int(line)
        for i in range(100000,700000):
            istr = str(i)
            for jstr in order_list:
                idstr_noV = istr + datestr + jstr
                V = get_check_digit(idstr_noV)
                if len(V) == 2 or V[-1] in doublelist:
                    continue
                idstr = idstr_noV + V
                idint = int(idstr)
                # print(idint,isPrime(idint))
                if isPrime(idint) == True:
                    # print(idint, isPrime(idint))
                    # result.append(idstr)
                    fw.write(idstr+"\n")

            # if isPrime(idint) == True:
            #     print('this num is',idint)
            #     result.append(idstr)
            # else:
            #     print('this num is', idint)



# print(result)

# with open("result.txt",'w') as fw:
#     for i in result:
#         fw.write(i+'\n')





# 101988185001020231 True
# 101988185001021373 True
# 101988185001021461 True
# 101988185001021541 True
# 101988 18500102 1779 True


