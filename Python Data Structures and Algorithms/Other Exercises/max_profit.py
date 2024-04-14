"""
You are given a list of integers representing stock prices for a certain company over a period of time, where each element in the list corresponds to the stock price for a specific day.

You are allowed to buy one share of the stock on one day and sell it on a later day.

Your task is to write a function called max_profit that takes the list of stock prices as input and returns the maximum profit you can make by buying and selling at the right time.

Note that you must buy the stock before selling it, and you are allowed to make only one transaction (buy once and sell once).

Constraints:



Each element of the input list is a positive integer representing the stock price for a specific day.



Function signature: def max_profit(prices):

Example:

Input: prices = [7, 1, 5, 3, 6, 4]
Function call: profit = max_profit(prices)
Output: profit = 5

Explanation: The maximum profit can be achieved by buying the stock on day 2 (price 1) and selling it on day 5 (price 6), resulting in a profit of 6 - 1 = 5.
"""

def max_profit(stock):
    aux = 0
    
    for i in range(len(stock)):
        for j in range(i + 1, len(stock)):
            if stock[i] != stock[j] and stock[j] > stock[i] and stock[j] - stock[i] > aux:
                aux = stock[j] - stock[i]
                
    return aux