# 121. Best Time to Buy and Sell Stock
# Topics: Array, Dynamic Programming
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float("inf")
        most_profit = 0
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                if profit > most_profit:
                    most_profit = profit
                    
        return most_profit