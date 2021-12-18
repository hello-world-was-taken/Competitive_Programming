#QUESTION
#https://leetcode.com/problems/max-number-of-k-sum-pairs/

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        arr_len = len(nums)
        
        i = 0
        j = arr_len - 1
        count = 0
        while (j > i and i < len(nums)):
            if nums[i] + nums[j] == k:
                i += 1
                j -= 1
                count += 1
            elif nums[i] + nums[j] > k:
                j -= 1
            else:
                i += 1
        
        return count
