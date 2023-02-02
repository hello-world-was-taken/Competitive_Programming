# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        operation_count = 0
        zeros = 0
        
        for i in range( n ):
            if nums[i] != 0:
                operation_count += 1
                for j in range( i + 1, n ):
                    nums[j] = max( 0, nums[j] - nums[i] )
            else:
                zeros += 1
            
            if nums[-1] == 0:
                return operation_count
            nums[i] = 0

        return len(nums) - zeros
                
