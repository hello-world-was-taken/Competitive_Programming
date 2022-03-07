#https://leetcode.com/problems/h-index-ii/



class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0 
        right = len(citations)
        best = 0
        while left < right:
            mid = sum([left, right])//2
            
            if citations[mid] < len(citations) - mid:
                left = mid + 1
            else:
                right = mid
        return len(citations) - left
