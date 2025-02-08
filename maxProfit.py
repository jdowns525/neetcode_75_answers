def maxProfit(prices):
    min_price = float('inf')  # Start with an infinitely high minimum price
    max_profit = 0  # Initialize max profit to zero
    for price in prices:
        # Update the minimum price if the current price is lower
        if price < min_price:
            min_price = price
        else:
            # Calculate profit if selling today and update max_profit if it's higher
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
    return max_profit

#Explanation:

#We keep updating the minimum price seen so far.
#For every price, we check if selling on that day (i.e., price - min_price) yields a better profit.
#Time Complexity: O(n)
#Space Complexity: O(1)
