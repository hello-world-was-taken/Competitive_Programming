#QUESTION
#https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        counted = []
        count = 1
        if len(nums) == 1:
            counted.append([count, nums[0]])
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                counted.append([count, nums[i-1]])
                count = 1
            if i == len(nums) -1:
                counted.append([count, nums[i]])
        counted.sort(reverse=True)
        print(counted)
        
        ans = []
        for i in range(k):
            ans.append(counted[i][-1])
            
        return ans
