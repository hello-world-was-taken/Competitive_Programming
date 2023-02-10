# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        
        count = 0
        
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums):
                if num1 + num2 == target and i != j:
                    count += 1
                    
        return count
