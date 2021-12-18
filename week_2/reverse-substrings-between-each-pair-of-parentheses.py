#QUESTION
#https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

class Solution:
    def first(self, s):
        stack = []
        arr_len = len(s)
        for i in range(arr_len - 1, -1, -1):
            if s[i] != '(':
                stack.append(s[i])
            else:
                self.reverse_upto(stack)

        stack.reverse()

        return self.to_string(stack)

    def reverse_upto(self, stack):
        stack_new = []
        while stack[-1] != ')':
            stack_new.append(stack.pop())
        
        stack.pop()

        for i in stack_new:
            stack.append(i)
            
    def to_string(self, stack):
        temp_ = ""
        for i in stack:
            temp_ += i
        return temp_
    
    def reverseParentheses(self, s: str) -> str:
        return self.first(s)
