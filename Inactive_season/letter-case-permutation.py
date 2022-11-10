https://leetcode.com/problems/letter-case-permutation/


class Solution:
    def backtrack(self, idx, curr, final_ans):
        if idx == len(curr):
            final_ans.add("".join(curr))
            return 
        
        if curr[idx].islower():
            curr[idx] = curr[idx].upper()
            self.backtrack(idx+1, curr, final_ans)
            curr[idx] = curr[idx].lower()
        
        if curr[idx].isupper():
            curr[idx] = curr[idx].lower()
            self.backtrack(idx+1, curr, final_ans)
            curr[idx] = curr[idx].upper()
        
        self.backtrack(idx + 1, curr, final_ans)
        
    def letterCasePermutation(self, s: str) -> List[str]:
        final_ans = set()
        self.backtrack(0, list(s), final_ans)
        return final_ans
