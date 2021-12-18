#QUESTION
#https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        arr_len = len(nums)
        len_l = len_r = len(l)
        new_list = []
        ans = []
        for i in range(len_l):
            new_list = nums[l[i]:r[i]+1]
            new_list.sort()
            d = new_list[1] - new_list[0]
            for i in range(1, len(new_list)):
                if new_list[i] - new_list[i-1] != d:
                    ans.append(False)
                    break
                elif (i == len(new_list) - 1):
                    ans.append(True)
            
        return ans
