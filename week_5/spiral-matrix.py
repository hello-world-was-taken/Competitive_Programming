#QUESTION
#https://leetcode.com/problems/spiral-matrix/

class Solution:     
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        isRight = True
        isDown = False
        isUp = False
        isLeft = False
        
        row_stop = 1
        col_stop = len(matrix[0]) - 1
        while len(matrix) > 0:
            if len(matrix) > 0 and isRight:
                temp = matrix.pop(0)
                for i in temp:
                    ans.append(i)
                isRight=False
                isDown= True
            if len(matrix) > 0 and isDown:
                for i in matrix:
                    if len(i) > 0:
                        ans.append(i.pop())
                isDown= False
                isLeft = True
            if len(matrix) > 0 and isLeft:
                temp = matrix.pop()
                temp.reverse()
                for i in temp:
                    ans.append(i)
                isLeft = False
                isUp = True
            if len(matrix) > 0 and isUp:
                for i in range(len(matrix)-1, -1, -1):
                    if len(matrix[i]) > 0:
                        ans.append(matrix[i].pop(0))
                isRight = True
                isup = False
        return ans
