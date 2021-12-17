#QUESTION
#https://leetcode.com/problems/valid-parentheses/

class Solution:
    
    def isValid(self, s: str) -> bool:
      
        dict_ = {
            '{': '}',
            '(': ')',
            '[':']'
        }
        
        my_stack = []
        for i in s:
            if i in dict_.keys():
                my_stack.append(i)
            if i in dict_.values():
                if len(my_stack) ==  0:
                    return False
                elif dict_[my_stack.pop()] != i:
                    return False
        if len(my_stack) > 0:
            return False
        return True
        
