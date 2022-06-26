# https://leetcode.com/problems/missing-number/
# todo: try it with bit manipulation



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return i+1
