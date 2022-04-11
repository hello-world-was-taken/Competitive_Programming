# https://leetcode.com/problems/house-robber/



class Solution:
    def rob(self, nums: List[int]) -> int:
        self.can_steal = True
        self.calc = {}
        def poss(index):
            if index == 0:
                return nums[0]
            if index == 1:
                return max(nums[0], nums[1])
            
            if index not in self.calc.keys():
                self.calc[index] = max(poss(index -1), poss(index -2) + nums[index])
            
            return self.calc[index]
        
        return poss(len(nums) - 1)
