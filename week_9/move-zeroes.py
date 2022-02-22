#https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr_len = len(nums)
        i = j = 0
        
        while j < arr_len and i < arr_len:
            if nums[i] != 0:
                i += 1
                j = i
                continue
            if nums[j] == 0:
                j += 1
                continue
            else:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
        return nums
