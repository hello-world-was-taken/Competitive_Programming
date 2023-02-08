# https://leetcode.com/problems/third-maximum-number/


class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        _max = float("-inf")
        unique_count = 0
        nums.sort( reverse=True )
        n = len( nums )
        
        for i in range( 0, n ):
            
            if _max != nums[i]:
                unique_count += 1
                _max = nums[i]
                
            if unique_count == 3:
                break
        if unique_count == 3:
            return _max
        return max( nums )
