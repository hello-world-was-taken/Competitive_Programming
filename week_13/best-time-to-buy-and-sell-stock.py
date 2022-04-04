# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _max = -1
        max_profit = 0
        for price in prices[::-1]:
            _max = max(_max, price)
            max_profit = max(max_profit, _max - price)
        return max_profit
                
        
        # n^2 solution but won't work obviously
#         profit = float("-inf")
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 profit = max( profit, prices[j] - prices[i])
                
#         return profit if profit > 0 else 0
