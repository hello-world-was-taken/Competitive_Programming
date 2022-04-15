# https://leetcode.com/problems/minimum-increment-to-make-array-unique/



class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        visited = set()
        moves = 0
        _max = 0
        
        for i in range(len(nums)):
            if nums[i] not in visited:
                visited.add(nums[i])
                _max = max(_max, nums[i])
            else:
                moves += abs(_max - nums[i] + 1)
                nums[i] += abs(_max - nums[i] + 1)
                _max = max(_max, nums[i])
                visited.add(nums[i])
                
        return moves
        
