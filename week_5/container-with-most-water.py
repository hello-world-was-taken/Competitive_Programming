#QUESTION
#https://leetcode.com/problems/container-with-most-water/
# The thing to note is that this unlike the histogram question, doesn't care about the next values. It just needs another block to pair up with.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        arr_len = len(height)
        i = 0
        j = arr_len -1
        g_max = 0
        current_max = 0
        while i < j:
            current_max = min(height[i], height[j]) * (j - i)
            g_max = max(g_max, current_max)
            
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return g_max
