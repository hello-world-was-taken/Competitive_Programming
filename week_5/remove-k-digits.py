#QUESTION
#https://leetcode.com/problems/remove-k-digits/
# The key point here is to remember that the popped elements need not be in a contagious memory.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        arr_len = len(num)
        
        
        popped_sofar = 0
        list_num = [None] * arr_len
        mono_stack = []
        for i, v in enumerate(num):
            list_num[i] = int(v)
        # print(list_num)
        i = 0
        while i < arr_len:
            if len(mono_stack) == 0:
                mono_stack.append(list_num[i])
                i += 1
                continue
            if popped_sofar < k and list_num[i] > mono_stack[-1]:
                mono_stack.append(list_num[i])
                
            else:
                while popped_sofar < k and len(mono_stack) > 0 and list_num[i] < mono_stack[-1]:
                    mono_stack.pop()
                    popped_sofar += 1
                mono_stack.append(list_num[i])
            i += 1
        print(mono_stack)
        while popped_sofar < k:
            mono_stack.pop()
            popped_sofar += 1
        
        a = ""
        for i in mono_stack:
            a += str(i)
        if a != "":
            to_int = int(a)
        
        if k >= len(num):
            return "0"
        return str(to_int) if len(str(to_int)) > 0 else "0"
