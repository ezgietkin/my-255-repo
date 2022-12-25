import random
import time
"""
start = time.time()

price_list = []

price_list = [19,4,18,5,6,3,8,2,12]
#for i in range(20000):
#    price_list.append(random.randint(1,2000000))

price = price_list.copy()
l = len(price_list)
profit_list = []
for i in range(l):
    for j in range(l-i):
        profit_list.append(price_list[-1] - price_list[j])
    del price_list[-1]
print(max(profit_list))
print(time.time()- start)
"""

def max_profit(price):
    l = len(price)
    profit_list = []
    for i in range(l):
        for j in range(l-i):
            profit_list.append(price[-1] - price[j])
        del price[-1]

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
        starttime = time.time()
        max_profit_quick(randomlist)
        endtime = time.time()
        totaltime = endtime - starttime
        sumtime = sumtime + totaltime
    avgtime2 = sumtime / 10
    sumtime = 0
    for i in range(10):
        starttime = time.time()
        max_profit(randomlist)
        endtime = time.time()
        totaltime = endtime - starttime
        sumtime = sumtime + totaltime
    avgtime1 = sumtime / 10
    #print(avgtime1)
    print(avgtime1, avgtime2)

print("start")
for k in range(1000, 1019):
    get_time(k)

print("no")
get_time(12162)