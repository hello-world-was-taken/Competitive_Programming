# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        i = 0
        ans = 0
        
        while i < len(s):
            if i + 1 < len(s) and roman[s[i+1]] > roman[s[i]]:
                ans += roman[s[i+1]] - roman[s[i]]
                i += 2
                continue
            else:
                ans += roman[s[i]]
                
            i += 1
                
        return ans
            
