prices = list(map(int,input("Enter prices : ").replace('[','').replace(']','').split(',')))
def maxProfit(prices):
    minprice = float('inf')
    maxprofit = 0
    for i in range(len(prices)):
        if prices[i] < minprice:
            minprice = prices[i]
        elif prices[i] - minprice > maxprofit:
            maxprofit = prices[i] - minprice
    return maxprofit
print(maxProfit(prices))