#QUESTION
#https://leetcode.com/problems/array-with-elements-not-equal-to-average-of-neighbors/

def rearrangeArray(self, nums):
    
    arr_len = len(nums) - 1
    
    # Other sorts result in Time Limit exceeded
    nums.sort()
    
    # For some reason this seems to work. Why? God knows
    
    for i in range(0, arr_len, 2):
        nums[i],nums[i+1]=nums[i+1],nums[i]
    
    return nums