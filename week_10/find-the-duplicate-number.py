#https://leetcode.com/problems/find-the-duplicate-number/


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans_max = max(nums)
        ans_range = [1, ans_max]
        count = 0
        
        while ans_range[0] < ans_range[1]:
            mid = sum(ans_range)//2
            for i in nums:
                if i > mid and i <= ans_range[1]:
                    count += 1
                    
            if count > ans_range[1] - mid:
                ans_range[0] = mid + 1
            else:
                ans_range[1] = mid
            
            count = 0
        
        return ans_range[0]
