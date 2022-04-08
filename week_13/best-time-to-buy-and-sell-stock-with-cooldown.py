# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/




class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        self.calculated = {}
        
        def best_buy(index, can_sell):
            if index >= len(prices):
                return 0
            
            if (index, can_sell) in self.calculated:
                return self.calculated[(index, can_sell)]
            
            if can_sell:
                self.calculated[(index, can_sell)] = max(prices[index] + best_buy(index + 2, False), best_buy(index + 1, True))
                return self.calculated[(index, can_sell)]
            else:
                self.calculated[(index, can_sell)] = max(best_buy(index + 1, True) - prices[index], best_buy(index + 1, False)) # I am buying now
                return self.calculated[(index, can_sell)]
        return best_buy(0, False)
        print(self.calculated)
