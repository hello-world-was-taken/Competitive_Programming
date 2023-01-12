# https://leetcode.com/problems/using-a-robot-to-print-the-lexicographically-smallest-string/

class Solution:
    def robotWithString(self, s: str) -> str:
        t = []
        ans = []
        next_best_min = list(s)
        n = len(s)
        best = s[-1]
        for i in range(len(s)-1, -1, -1):
            best = min(best, s[i])
            next_best_min[i] = best
            
        for i in range(n):
            if next_best_min[i] < s[i]:
                while len(t) and t[-1] <= next_best_min[i]:
                    ans.append(t.pop())
                t.append(s[i])
            else:
                while len(t) and t[-1] <= s[i]:
                    ans.append(t.pop())
                ans.append(s[i])
        while len(t):
            ans.append(t.pop())
        return "".join(ans)
