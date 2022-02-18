#https://leetcode.com/problems/remove-duplicates-from-sorted-array/


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        arr_len = len(nums)
        i = 0
        j = 1
        duplicate_count = 0
        while j < arr_len and i < arr_len:
            if nums[j] == nums[i]:
                j += 1
                duplicate_count += 1
                continue
            if nums[j] != nums[i] and duplicate_count > 0:
                nums[i + 1] = nums[j]
                i += 1
                j += 1
                continue
            if nums[j] != nums[i]:
                i += 1
                j += 1
        return i + 1
