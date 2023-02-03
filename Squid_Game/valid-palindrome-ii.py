# https://leetcode.com/problems/valid-palindrome-ii/


class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        
        def isPali(left, right):
            while left < right and right < n:
                if s[ left ] == s[ right ]:
                    left += 1
                    right -= 1
                else:
                    return left, right, False
            return -1, -1, True
        
        left, right, pali = isPali(0, n-1)
        if not pali:
            return isPali(left + 1, right)[2] or isPali(left, right - 1)[2]
        return True
                
