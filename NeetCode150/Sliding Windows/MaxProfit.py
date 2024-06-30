def maxProfit(prices):
    # East: simply track lowest price and compare to profit made if you were to sell each day
    lowest = 0 
    profit = 0 
    for r in range(1, len(prices)):
        if prices[r] < prices[lowest]:
            lowest = r 
        profit = max( profit, prices[r] - prices[lowest])
    return profit