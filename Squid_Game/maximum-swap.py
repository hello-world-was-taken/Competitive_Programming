# https://leetcode.com/problems/maximum-swap/


class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str( num ))
        n = len( num )
        next_max_greater = [float("-inf") for i in range( n )]
        _max_idx = n - 1
        
        for i in range(n - 1, -1, -1):
            curr = num[i]
            if curr > num[_max_idx]:
                _max_idx = i
                
            next_max_greater[i] = _max_idx
        
        for i in range( n ):
            curr = num[i]
            next_greater_idx = next_max_greater[i]
            if curr < num[next_greater_idx]:
                num[i], num[next_greater_idx] = num[next_greater_idx], num[i]
                break
                
        return int("".join(num))
        
        
