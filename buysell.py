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
arr=[7,1,5,3,12,4]

def buysell(arr):
    max_profit=0
    mini=arr[0]
    for x in range(1,len(arr)):
        cost=arr[x]-mini
        max_profit=max(max_profit,cost)
        mini=min(mini,arr[x])
    return max_profit
print(buysell(arr))

#best time to buy and sell stocks
arr = [8, 2, 5, 3, 1, 9]

def max_profit(prices):
    max_profit = 0
    min_price = prices[0]
    for price in prices[1:]:
        profit = price - min_price
        max_profit = max(max_profit, profit)
        min_price = min(min_price, price)
    return max_profit
    
print(max_profit(arr))