# https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/



class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        count = 0
        count_to_be_added = 0
        i = 0
        j = 1
        while i < len(prices) and j < len(prices):
            if prices[i] - prices[j] == 1:
                count += 1
                count_to_be_added += 1
            else:
                count_to_be_added -= 1
                count += (count_to_be_added * (count_to_be_added + 1)) // 2
                count_to_be_added = 0
            i += 1
            j += 1
            
        count_to_be_added -= 1
        count += (count_to_be_added * (count_to_be_added + 1)) // 2
        
        if len(prices) > 1:
            return count + len(prices)
        else:
            return 1
