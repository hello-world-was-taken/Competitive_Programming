# https://leetcode.com/problems/set-mismatch/


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        ans = ["", ""]
        for i in range(1, len(nums) + 1):
            if i not in count:
                ans[1] = i
            elif count[i] == 2:
                ans[0] = i
                

        return ans
