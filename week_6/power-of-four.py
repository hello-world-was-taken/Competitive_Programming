#https://leetcode.com/problems/power-of-four/

class Solution:
    def helper(self, n):
        if n == 1:
            return True
        if n%4 != 0:
            return False
        else:
            return self.helper(n//4)
        
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        else:
            return self.helper(n)
