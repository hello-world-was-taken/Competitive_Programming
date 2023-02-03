# https://leetcode.com/problems/random-pick-with-weight/


import random

class Solution:

    def __init__(self, w: List[int]):
        self.w = w
        n = len(w)
        
        _sum = sum( self.w )
        for i in range( n ):
            self.w[i] = self.w[i] / _sum
            
        for i in range( 1, n ):
            self.w[i] += self.w[i-1]
        

    def pickIndex(self) -> int:
        normal = random.uniform(0, 1)

        for idx, weight in enumerate( self.w ):
            if normal <= weight:
                return idx
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
