#QUESTION
#https://leetcode.com/problems/number-of-good-pairs/

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums.sort()
        
        i = 0
        j = 0
        count = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if(nums[i] == nums[j]):
                    count += 1
        return count
                
