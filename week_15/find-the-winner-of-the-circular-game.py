# https://leetcode.com/problems/find-the-winner-of-the-circular-game/



class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        
        li = [i for i in range(1, n+1)]
        tk = k
        non_zero = n
        i = 0
        _max = -1
        while non_zero > 1:
            if li[i] == -1:
                i = (i+1) % len(li) # wrap around 
                continue    # already lost
            _max = max(_max, li[i])
            tk -= 1
            
            if tk == 0:
                li[i] = -1 # checked   
                tk = k
                non_zero -= 1
                
            i = (i+1) % len(li) # wrap around 
        return _max
    
