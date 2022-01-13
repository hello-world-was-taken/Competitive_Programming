#Question
#https://leetcode.com/problems/k-th-symbol-in-grammar/

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        above = self.kthGrammar(n-1, (k // 2) + (k % 2))
        if above == 0:
            return 1 if k % 2 == 0 else 0
        else:
            return 0 if k % 2 == 0 else 1
