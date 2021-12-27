#QUESTION
#https://leetcode.com/problems/largest-rectangle-in-histogram/


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        arr_len = len(heights)
        g_max = 0
        i = 1
        mono_stack = []
        mono_stack.append((heights[0], 0))
        while i < arr_len:
            if heights[i] >= mono_stack[-1][0]:
                mono_stack.append((heights[i], i))
            else:
                last_e = None
                while(len(mono_stack) > 0 and mono_stack[-1][0] > heights[i]):
                    last_e = mono_stack.pop()
                    temp_max = (i - last_e[1]) * last_e[0]
                    
                    if temp_max > g_max:
                        g_max = temp_max
                mono_stack.append((heights[i], last_e[1]))
            i += 1
            
        if len(mono_stack) > 0:
            j = 0
            mono_stack_len = len(mono_stack)
            while j < mono_stack_len:
                temp_max = (arr_len - mono_stack[j][1]) * mono_stack[j][0]
                if temp_max > g_max:
                    g_max = temp_max
                j += 1
        return g_max
