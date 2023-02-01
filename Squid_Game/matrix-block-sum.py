# https://leetcode.com/problems/matrix-block-sum/


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        prefix = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for r in range(m):
            _sum = 0
            for c in range(n):
                prefix[r+1][c+1] = prefix[r][c+1] + prefix[r + 1][c] + mat[r][c] - prefix[r][c]
            
            
        m, n = len(mat), len(mat[0])
        answer = [[0 for _ in range(n)] for _ in range(m)]

        for r in range(m):
            for c in range(n):
                rs, re = max(r - k, 0), min(r + k, m - 1)
                cs, ce = max(c - k, 0), min(c + k, n - 1)
                answer[r][c] = prefix[re+1][ce+1] - prefix[rs][ce+1] - prefix[re+1][cs] + prefix[rs][cs]
                
        return answer
