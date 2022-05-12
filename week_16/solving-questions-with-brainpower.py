# https://leetcode.com/problems/solving-questions-with-brainpower/



class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @lru_cache(None)
        def helper(index):
            
            if index >= len(questions):
                return 0
            
            res = questions[index][0] + helper(index + questions[index][1] + 1)
            res_2 = helper(index + 1)
            
            return max(res, res_2)
        return helper(0)
