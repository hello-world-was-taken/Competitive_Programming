# https://leetcode.com/problems/find-pivot-index/



class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        right_sum = sum(nums)
        left_sum = 0
        right_sum -= nums[0]
        if len(nums) == 1:
            return 0
        for i in range(len(nums)-1):
            if left_sum == right_sum:
                return i
            else:
                left_sum += nums[i]
                right_sum -= nums[i+1]
        if left_sum == right_sum:
                return i + 1
        return -1
