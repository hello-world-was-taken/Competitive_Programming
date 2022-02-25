#https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # nums.sort()
        summation = 0
        smallest_divisor = 0
        left = 1
        right = max(nums)
        
        while left <= right:
            mid = sum([left + right])//2
            for i in nums:
                summation += math.ceil(i/mid)
            
            if summation <= threshold:
                smallest_divisor = mid
                right = mid - 1
            else:
                left = mid + 1
            
            summation = 0
        
        return smallest_divisor
