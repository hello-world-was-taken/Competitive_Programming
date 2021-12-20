#QUESTION
#https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        arr_len = len(nums)
        ans = [0] * arr_len
        j = 0
        for i in range(0, arr_len, 2):
            ans[i] = nums[j]
            j += 1
        i = 1
        count = 0
        for j in range(arr_len -1 , 0, -1):
            ans[i] = nums[j]
            i += 2
            count += 1
            if (count >= (arr_len // 2)):
                break
        maxi = 0
        for i in range(1, arr_len, 2):
            maxi = max(maxi, (ans[i-1] + ans[i]))
        return maxi
