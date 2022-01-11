#QUESTION
#https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        arr_len = len(citations)
        citations.sort(reverse=True)        
        i = 0
        if citations[0] == 0:
            return 0
        while i < arr_len:
            if len(citations) -1 == i:
                return i + 1
            if citations[i+1] <= i+1:
                return i + 1
            i += 1
