#https://leetcode.com/problems/kth-largest-element-in-an-array/


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        i = 0
        # j = 0
        # heap = []
        while i < len(nums):
            nums[i] = -nums[i]
            i += 1
        heapq.heapify(nums)
        i = 0
        while i < k:
            maxi = -(heapq.heappop(nums))
            i += 1
        return maxi
