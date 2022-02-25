#https://leetcode.com/problems/last-stone-weight/


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for i in stones:
            heapq.heappush(heap, -i)
            
        greatest = None
        n_greatest = None
        while len(heap) > 2:
            greatest = heapq.heappop(heap)
            if len(heap) > 0:
                n_greatest =heapq.heappop(heap)
                
            if greatest != n_greatest:
                temp = -greatest + n_greatest
                heapq.heappush(heap, -temp)
                # print(heap)
                
        if len(heap) == 2:
            greatest = heapq.heappop(heap)
            n_greatest =heapq.heappop(heap)
            if greatest != n_greatest:
                temp = -greatest + n_greatest
                heapq.heappush(heap, -temp)
                
        return -heap[0] if len(heap) > 0 else 0
