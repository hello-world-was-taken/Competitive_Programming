# https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/



class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        
        zero_count = 0
        _count = 0
        for i in range(len(s)):
            if locked[i] == '0':
                zero_count += 1
                continue
            if s[i] == '(':
                _count += 1
            if s[i] == ')':
                _count -= 1
                if _count < 0 and zero_count <= 0:
                    return False
                elif _count < 0 and zero_count > 0:
                    zero_count -= 1
                    _count += 1
                    
            
        # we could have done it using a single loop and different zero_count
        # and _count, but it is unneccessary
        zero_count = 0
        _count = 0
        for i in range(len(s)-1, -1, -1):
            if locked[i] == '0':
                zero_count += 1
                continue
            if s[i] == '(':
                _count -= 1
                if _count < 0 and zero_count <= 0:
                    return False
                elif _count < 0 and zero_count > 0:
                    zero_count -= 1
                    _count += 1
            if s[i] == ')':
                _count += 1
                    
        
        
        if _count:
            if zero_count:
                zero_count -= _count
                if zero_count < 0:
                    return False
        if zero_count % 2 == 1:
            return False
        
        return True
                    
        
