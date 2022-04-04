# https://leetcode.com/problems/rotate-array/



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < k:
            k %= len(nums)
            
        to_be_rotated = [None] * k
        j = 0
        
        for i in range(len(nums)-k, len(nums)):
            to_be_rotated[j] = nums[i]
            j += 1
        
        for i in range(len(nums)-k-1, -1,-1):
            nums[i+k] = nums[i]
        
        for i in range(k):
            nums[i] = to_be_rotated[i]
        
        
