# https://leetcode.com/problems/subarray-sum-equals-k/



class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] = 1 # we assume we have a zero to consider if nums[i] == k
        curr_max = 0
        count = 0
        
        for i in range(len(nums)):
            curr_max += nums[i]
            
            if curr_max - k in prefix:
                count += prefix[curr_max-k]
                
            prefix[curr_max] += 1
        return count
