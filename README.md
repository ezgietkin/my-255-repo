def max_profit_quick (price):
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
            max_changed=True
        if max_changed:
            dif = max - min
            if dif > profit:
                profit = dif
    print(profit)
max_profit_quick([19,4,18,5,6,3,8,2,12])