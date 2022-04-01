# https://leetcode.com/problems/triangle/



class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
      
        # bottom up
#         for i in range(len(triangle)-1, -1, -1):
#             for j in range(len(triangle[i])-1):
#                 triangle[i-1][j] += min(triangle[i][j], triangle[i][j+1])
        
#         return(triangle[0][0])



        # top down
        dic = {}
        def find_best(row, col):
            if (row, col) not in dic:
                if 0 <= row < len(triangle) and 0 <= col < len(triangle[row]):
                    best = find_best(row +1, col)
                    second = min(best, find_best(row +1, col +1))
                    ans = min(best, find_best(row +1, col +1)) + triangle[row][col]
                    dic[(row, col)] = ans
                    return ans
                return 0
            else:
                return dic[(row, col)]
        
        return find_best(0,0)
