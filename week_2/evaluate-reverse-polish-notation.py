#QUESTION
#https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr_len = len(tokens)
        stack_ = [0] * arr_len
        
        # for i in range(arr_len):
        #     stack_[i] = tokens.pop()
        # print(stack_)
        
        
                
        i = 0
        while(i < len(tokens)):
            if tokens[i] == "+":
                result = int(tokens[i-2]) + int(tokens[i-1]) 
                # print(int(tokens[i-2]), " + ", int(tokens[i-1]), " ", result)
               
                tokens[i-2] = result
                # print(int(tokens[i-2]), " + ", int(tokens[i-1]), " ", result)
                tokens.pop(i-1)
                tokens.pop(i-1)
                # print(tokens)
                i -= 2
            if tokens[i] == "-":
                result = int(tokens[i-2]) - int(tokens[i-1])
                # print(int(tokens[i-2]), " - ", int(tokens[i-1]), " ", result)
              
                tokens[i-2] = result
                tokens.pop(i-1)
                tokens.pop(i-1)
                # print(tokens)
                i -= 2
            if tokens[i] == "*":
                result = int(tokens[i-2]) * int(tokens[i-1])
                # print(int(tokens[i-2]), " * ", int(tokens[i-1]), " ", result)
                
                tokens[i-2] = result
                tokens.pop(i-1)
                tokens.pop(i-1)
                # print(tokens)
                i -= 2
            if tokens[i] == "/":
                result = math.trunc(int(tokens[i-2]) / int(tokens[i-1]))
                # if result < 0:
                #     result = 0
                # print(int(tokens[i-2]), " / ", int(tokens[i-1]), " ", result)
                
                tokens[i-2] = result
                tokens.pop(i-1)
                tokens.pop(i-1)
                # print(tokens)
                i -= 2
            i += 1
            
        return tokens[0]
