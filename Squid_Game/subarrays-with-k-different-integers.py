# https://leetcode.com/problems/subarrays-with-k-different-integers/


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        unique = 0
        subarray_count = 0
        intermediaries = 0
        n = len( nums )
        
        l = 0
        for r in range( n ):
            curr = nums[r]
            if count[curr] == 0:
                unique += 1
            if curr not in count:
                count[curr] += 1
                unique += 1
            else:
                count[curr] += 1

            if unique > k:
                count[nums[l]] -= 1
                l += 1
                unique -= 1
                intermediaries = 0
                
            while count[nums[l]] > 1:
                intermediaries += 1
                count[nums[l]] -= 1
                l += 1
            
            if unique == k:
                subarray_count += intermediaries + 1
        
        return subarray_count
