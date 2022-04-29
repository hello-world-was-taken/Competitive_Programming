# https://leetcode.com/problems/count-number-of-nice-subarrays/



class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if not nums[i] % 2:
                nums[i] = 0
                
        found = 0
        odd = 0
        for i in range(len(nums)):
            
            if nums[i] != 0:
                odd += 1
            nums[i] = odd
        # print("nums: ", nums)
        
        dic = defaultdict(lambda: [0, 0])
        for i, val in enumerate(nums):
            if val >= k:
                dic[val][0] = i
                dic[val][1] += 1
        
        passed = 0       
        nice = 0
        
        for val in nums:
            
            if k+passed in dic:
                nice += dic[k+passed][1]
            
            if val == (passed + 1):
                passed += 1
                
        return nice
