#QUESTION
#https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        arr_len = len(nums)
        
        i = j = 0
        
        mini = maxi = count = 0
        inc_queue = []
        dec_queue = []
        
        while i < arr_len and j < arr_len:
            if len(inc_queue) == 0:
                inc_queue.append([nums[j], j])
            else:
                while len(inc_queue) > 0 and inc_queue[-1][0] > nums[j]:
                    # print(nums[i])
                    inc_queue.pop()
                inc_queue.append([nums[j], j])
                
            if len(dec_queue) == 0:
                dec_queue.append([nums[j], j])
            else:
                while len(dec_queue) > 0 and dec_queue[-1][0] < nums[j]:
                    dec_queue.pop()
                dec_queue.append([nums[j], j])
            
            if abs(dec_queue[0][0] - inc_queue[0][0]) <= limit:
                if ((j - i + 1) > count):
                    count = j - i + 1
                j += 1
            else:
                i += 1
                while len(dec_queue) > 0 and dec_queue[0][1] < i:
                    dec_queue.pop(0)
                while len(inc_queue) > 0 and inc_queue[0][1] < i:
                    inc_queue.pop(0)
                
        return (count)
