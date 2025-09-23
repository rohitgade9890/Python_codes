#find best time to buy and sell the stock so you can maximize profit
arr=[7,1,5,3,12,4]
def buysell(arr):
    max_profit=float('-inf')
    buy_at=-1
    sell_at=-1
    for x in range(len(arr)):
        current_profit=0
        for y in range(x+1,len(arr)):
            current_profit = arr[y] - arr[x]
            if current_profit > max_profit:
                max_profit=current_profit
                but_at=x
                sell_at=y
    return ['if you buy stock at {0}$ and sell at {1}$ you will get max_profit of {2}$'.format(arr[but_at],arr[sell_at],max_profit)]
print(buysell(arr))

#optimized
prices=[7,1,5,3,12,4]     
def maximumProfit(prices):
    mini = prices[0]
    maxProfit = 0
    
    for i in range(1,len(prices)):
        cost = prices[i] - mini
        maxProfit = max(maxProfit, cost)
        mini = min(mini, prices[i])
    
    return maxProfit
print(maximumProfit(prices))