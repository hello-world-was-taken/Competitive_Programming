#https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_ship_capacity = sum(weights)
        left = 0
        right = max_ship_capacity
        
        min_capacity = 0
        
        while left <= right:
            mid = sum([left, right])//2
            temp_mid = mid
            no_of_days_taken = 1
            i = 0
            while i < len(weights):
                if mid < weights[i]:
                    no_of_days_taken = -1
                    break
                temp_mid -= weights[i]
                if temp_mid < 0:
                    no_of_days_taken += 1
                    temp_mid = mid
                    i -= 1
                i += 1
            if no_of_days_taken > days or no_of_days_taken == -1:
                left = mid + 1
            else:
                min_capacity = mid
                right = mid - 1
            
        return min_capacity
