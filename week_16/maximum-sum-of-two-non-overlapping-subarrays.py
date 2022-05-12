# https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/



class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        overlap = lambda f, s: s[0] <= f[0] <= s[1] or s[0] <= f[1] <= s[1] or f[0] <= s[0] <= f[1] or f[0] <= s[1] <= f[1]
        
        first = []
        second = []
        prefix = [0] * len(nums)
        
        prefix[0] = nums[0]
        
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        
        first_len_max = []
        second_len_max = []
        
        for i in range(firstLen - 1, len(nums)):
            start = -1
            initial = 0
            if (i - firstLen) > -1:
                initial = prefix[i-firstLen]
                start = i - firstLen
            first_len_max.append((prefix[i] - initial, (start+1, i)))
            
        
        for j in range(secondLen - 1, len(nums)):
            start = -1
            initial = 0
            if j - secondLen >= 0:
                initial = prefix[j-secondLen]
                start = j - secondLen
            second_len_max.append((prefix[j] - initial, (start+1, j)))
            
        first_len_max.sort(key=lambda x: x[0])
        second_len_max.sort(key=lambda x: x[0])
            
        choice = -1
        for j in range(len(second_len_max)-1, -1, -1):
            for i in range(len(first_len_max)-1, -1, -1):
                if not overlap(first_len_max[i][1], second_len_max[j][1]):
#                     if first_len_max[i][0] + second_len_max[j][0] == 108:
#                         print("first: ", first_len_max[i][1], "second: ", second_len_max[j][1])
                    choice = max(first_len_max[i][0] + second_len_max[j][0], choice)
                    break
                
        return choice
         
        
        
        
        
        
        
