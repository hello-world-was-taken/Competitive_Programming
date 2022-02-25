#https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/



"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans_list = []
        nums = [0] * 1000
        for i, v in enumerate(range(1, 1001)):
            nums[i] = v
        # print(value[-1])
        # return
        for i in range(1, 1001):
            left = 0
            right = 1000
            while left <= right:
                mid = sum([left, right])//2
                if customfunction.f(i,nums[mid]) == z:
                    ans_list.append([i,nums[mid]])
                    break
                elif customfunction.f(i,nums[mid]) < z:
                    left = mid + 1
                else:
                    right = mid -1
                    
        return ans_list
