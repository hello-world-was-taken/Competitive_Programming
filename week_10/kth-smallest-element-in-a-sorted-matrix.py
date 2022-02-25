#https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/



class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i, row in enumerate(matrix):
            heapq.heappush(heap, (row[0], i, 0))

        count = 0
        ans = None
        while count < k:
            ans = heapq.heappop(heap)
            row = matrix[ans[1]]
            if (ans[2] + 1) == len(row):
                count += 1
                continue
            val = row[ans[2] + 1]
            heapq.heappush(heap, (val, ans[1], ans[2]+1))
            count += 1
        
        return ans[0]
