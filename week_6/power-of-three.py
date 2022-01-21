#https://leetcode.com/problems/power-of-three/

class Solution:
    def helper(self, n):
        if n == 1:
            return True
        if n%3 != 0:
            return False
        else:
            return self.helper(n//3)
    def isPowerOfThree(self, n: int) -> bool:
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            return self.helper(n)
