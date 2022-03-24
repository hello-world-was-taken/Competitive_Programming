# About to sleep n^2 solution. Optimiza tomorrow!
# https://leetcode.com/problems/sum-of-subarray-ranges/




class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        min_max_until = defaultdict(int)
        ans = 0
        
        for i in range(len(nums)):
            mini = float("inf")
            maxi = float("-inf")
            
            for j in range(i, len(nums)):
                mini = min(nums[j], mini)
                maxi = max(nums[j], maxi)
                
                ans += maxi - mini
        return ans
