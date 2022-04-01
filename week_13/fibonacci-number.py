# https://leetcode.com/problems/fibonacci-number/



class Solution:
    def fib(self, n: int) -> int:
        one = 1
        two = 1
        
        for i in range(2, n):
            temp = one
            one = two
            two = one + temp
        return two if n > 0 else 0
