# https://leetcode.com/problems/number-of-ways-to-select-buildings/


class Solution:
    def numberOfWays(self, s: str) -> int:
        n = len( s )
        zeros_before = []
        ones_before = []
        zero_before_count = zero_after_count = 0
        one_before_count = one_after_count = 0
        total = 0
        
        for building in s:
            zeros_before.append( zero_before_count )
            if building == '0':
                zero_before_count += 1

        for i in range(n-1, -1, -1):
            building = s[i]
            
            if building == '1':
                total += zeros_before[i] * zero_after_count
            elif building == '0':
                zero_after_count += 1      
        
        
        for building in s:
            ones_before.append( one_before_count )
            if building == '1':
                one_before_count += 1

        for i in range(n-1, -1, -1):
            building = s[i]
            
            if building == '0':
                total += ones_before[i] * one_after_count
            elif building == '1':
                one_after_count += 1
                
        return total
