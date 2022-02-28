#https://leetcode.com/problems/search-in-rotated-sorted-array/



class Solution:
    def find_pivot(self, nums):
        left = 0
        right = len(nums) -1 
        best = right
        while left <= right:
            mid = sum([left, right])//2
            if nums[mid] > nums[right]:
                left = mid +1
            elif nums[mid] < nums[best]:
                best = mid
                right = mid - 1
            else:
                return best if nums[mid] >= nums[best] else mid
            
        return best
    
    def find_num(self, search_range, nums, target):
        left, right = search_range
        
        while left <= right:
            mid = sum([left, right])//2
            
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
    
    def search(self, nums: List[int], target: int) -> int:
        pivot = self.find_pivot(nums)
        if pivot != 0:
            res = self.find_num((0, pivot-1), nums, target)
            return res if res != -1 else self.find_num((pivot, len(nums)-1), nums, target)
        else:
            return self.find_num((0, len(nums)-1), nums, target)
        
        
