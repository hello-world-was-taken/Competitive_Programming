# https://leetcode.com/problems/predict-the-winner/



class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        self.can_win = True
        
        # max_min approach
        @lru_cache
        def helper(l, r, p1_turn):
            if l == r+1: # if i > r then the list has been traversed
                return 0
            if p1_turn:
                return max(nums[l] + helper(l+1, r, not p1_turn), nums[r] + helper(l, r-1, not p1_turn))
            else:
                return min(helper(l+1, r, not p1_turn), helper(l, r-1, not p1_turn))
            
        p1_score = helper(0, len(nums)-1, True)
        p2_score = sum(nums) - p1_score
        
        return p1_score >= p2_score
