#QUESTION
#https://leetcode.com/problems/count-good-numbers/

class Solution:
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n % 2 == 0:
            temp = self.myPow(x, n//2)
            return (temp * temp) % (10**9 + 7)
        else:
            return (x * self.myPow(x, n-1)) % (10**9 + 7)
    def countGoodNumbers(self, n: int) -> int:
        odd = self.myPow(4, n//2)
        even = self.myPow(5, (n//2 + n%2))
        return (odd * even) % (10**9 + 7)
