#QUESTION
#https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n >= 0:
            if n == 0:
                return 1
            elif n % 2 == 0:
                temp = self.myPow(x, n//2)
                return temp * temp
            else:
                return x * self.myPow(x, n-1)
        elif n < 0:
            return 1 / self.myPow(x, abs(n))
