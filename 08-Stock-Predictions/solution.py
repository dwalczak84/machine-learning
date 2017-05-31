import numpy as np
import math

def stochastic_oscillator(prices, period):
    min_p = prices[-period:].min()
    max_p = prices[-period:].max()

    if min_p == max_p:
        return 0.

    return abs(100. * (prices[-1] - min_p) / (max_p - min_p))

def printTransactions(m, k, d, name, owned, prices):
    output = []

    prices = np.array(prices)
    deviations = prices.std(1)

    to_buy = []
    for i in reversed(np.argsort(deviations)):
        sa = stochastic_oscillator(prices[i], 3)

        if sa >= 80. and owned[i]:
            output.append("%s %s %s" % (
                name[i], 'SELL', owned[i]))

        elif sa <= 20. and m:
            to_buy.append((i, sa, prices[i][-1]))

    for i, sa, price in to_buy:
        num = int(m / int(math.ceil(price)))
        if num:
            output.append("%s %s %s" % (
                name[i], 'BUY', num))
            m -= (num * int(math.ceil(price)))

    return output

if __name__ == '__main__':
    m, k, d = [float(i) for i in raw_input().strip().split()]
    k = int(k)
    d = int(d)
    names = []
    owned = []
    prices = []
    for data in range(k):
        temp = raw_input().strip().split()
        names.append(temp[0])
        owned.append(int(temp[1]))
        prices.append([float(i) for i in temp[2:7]])
    
    output = printTransactions(m, k, d, names, owned, prices)
    
    print len(output)
    
    for line in output:
        print line
