#QUESTION
#https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        arr_len1 = len(nums1)
        arr_len2 = len(nums2)
        mono_stack = []
        dic = {}
        for i in range(arr_len2):
            if len(mono_stack) == 0:
                mono_stack.append(nums2[i])
                continue
            if nums2[i] > mono_stack[-1]:
                while len(mono_stack) > 0 and nums2[i] > mono_stack[-1]:
                    dic[mono_stack.pop()] = nums2[i]
            mono_stack.append(nums2[i])
        for i in mono_stack:
            dic[i] = -1
        ans = [0] * arr_len1
        for i in range(arr_len1):
            ans[i] = dic[nums1[i]]
        return ans
