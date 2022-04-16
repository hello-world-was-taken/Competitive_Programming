# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/



class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        heap = []
        
        for i in range(1, len(nums)):
            prefix[i] += prefix[i-1] + nums[i]
        
        
        best = float("inf")
        
        i = 0
        
        while i < len(nums):
            if nums[i] >= k:
                best = min(best, 1)
                
            if prefix[i] >= k:
                best = min(best, i+1)
                
            while len(heap) and prefix[i] - heap[0][0] >= k:
                best = min(best, abs(heappop(heap)[1] - i))
            
            heappush(heap, (prefix[i], i))
            
            
            i += 1
            
        return best if best < float("inf") else -1
