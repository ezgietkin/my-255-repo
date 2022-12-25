import time
import random

def max_profit(price):
    starttime = time.time()
    l = len(price)
    max = 0
    for i in range(l):
        b = price[i]
        for j in range(l-i):
            s = price[j]
            dif = s - b
            if dif > max:
                max = dif
    endtime = time.time()
    totaltime = endtime - starttime
    sumtime = sumtime + totaltime
    avgtime2 = sumtime / 10
    print(avgtime2)
    return dif

def max_profit_quick(price):
    min = price[0]
    max = price[0]
    profit = 0
    for i in price:
        max_changed = False
        if i < min:
            min = i
            max = min
        if i > max:
            max = i
            max_changed = True
        if max_changed:
            dif = max - min
            if dif > profit:
                profit = dif

def get_time(n):
    randomlist = []
    for i in range(n):
        number = random.randint(0, 10*n)
        randomlist.append(number)
    sumtime = 0
    for i in range(10):
        max_profit(randomlist)
"""
print("start")
for k in range(4000, 4019):
    get_time(k)
"""
print("no")
get_time(421620)