# https://leetcode.com/problems/decode-string/



class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        mul = 0
        i = 0
        while i < len(s):
            if s[i].isnumeric():
                mul += int(s[i])
                
                if i + 1 < len(s) and s[i+1].isnumeric():
                    mul = (mul * 10) + int(s[i + 1])
                    i += 1
                    
                    if i + 1 < len(s) and s[i+ 1].isnumeric():
                        mul = (mul * 10) + int(s[i + 1])
                        i += 1
                stack.append(mul)
                i += 1
                mul = 0
                continue
                        
            elif s[i] == ']':
                times = 1
                temp = []
                
                while stack[-1] != '[':
                    temp.append(stack.pop())
                temp.reverse()
                
                if len(stack):
                    stack.pop() # poping the '['
                    
                    if isinstance(stack[-1], int):
                        times = stack.pop()
                        
                stack.append(times * "".join(temp)) 

            else:
                stack.append(s[i])
            
            i += 1  

        return "".join(stack)
