#Example:
#Input: [7,1,5,3,6,4] → Output: 5 (buy at 1, sell at 6)
def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit
