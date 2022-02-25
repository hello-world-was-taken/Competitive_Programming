#https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        left_index = -1
        right_index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left_index = mid
                right = mid - 1
         
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right_index = mid
                left = mid + 1
                
        return [left_index, right_index]
