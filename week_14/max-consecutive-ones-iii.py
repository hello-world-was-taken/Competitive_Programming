# https://leetcode.com/problems/max-consecutive-ones-iii/



class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = j = 0
        _max = 0
        
        if nums[i] == 0 and k > 0:
                k -= 1
                _max += 1
        elif nums[i] == 0 and k == 0:
            while i < len(nums) and nums[i] == 0:
                i += 1
        
        j = i + 1
        while j < len(nums):
            if nums[j] == 0 and k > 0:
                k -= 1
            elif nums[j]  == 0 and k == 0:
                if nums[i] == 0:
                    k += 1
                i += 1
                continue
            _max = max(_max, j - i + 1)  
            j += 1
            
        return _max
