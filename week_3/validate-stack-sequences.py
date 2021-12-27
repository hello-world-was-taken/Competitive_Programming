#QUESTION
#https://leetcode.com/problems/validate-stack-sequences/


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        arr_len_pushed = len(pushed)
        arr_len_popped = len(popped)
        i = j = 0
        stack = []
        j_stopped = -1
        while i < arr_len_pushed and j < arr_len_popped:
            if len(stack) > 0 and stack[-1] == popped[j]:
                stack.pop()
                j += 1
                j_stopped = j
                continue
            if pushed[i] != popped[j]:
                stack.append(pushed[i])
                i += 1
            elif popped[j] == pushed[i]:
                i += 1
                j += 1
            else:
                j += 1
            j_stopped = j
        while j_stopped < arr_len_popped:
            if stack[-1] != popped[j_stopped]:
                return False
            stack.pop()
            j_stopped += 1
        return True
