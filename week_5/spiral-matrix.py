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
    
    
    # More efficient solution to the question using 2 variables and a pointer.
    class Solution:     
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        isRight = True
        isDown = False
        isUp = False
        isLeft = False
        
        curr_index = [0,-1]
        row = len(matrix)
        col = len(matrix[0])
        while row > 0 and col > 0:
            # print(curr_index)
            if col > 0 and isRight:
                for i in range(col):
                    # print("isRight: ", curr_index, row, col)
                    curr_index[1] += 1
                    ans.append(matrix[curr_index[0]][curr_index[1]])
                row -= 1
                isRight=False
                isDown= True
                isUp = False
                isLeft = False
            
            
            if row > 0 and isDown:
                for i in range(row):
                    # print("isDown: ", curr_index, row, col)
                    curr_index[0] += 1
                    ans.append(matrix[curr_index[0]][curr_index[1]])
                col -= 1
                isDown= False
                isLeft = True
                isRight=False
                isUp = False
            
            
            if col > 0 and isLeft:
                for i in range(col):
                    # print("isLeft: ", curr_index, row, col)
                    curr_index[1] -= 1
                    ans.append(matrix[curr_index[0]][curr_index[1]])
                row -= 1
                isLeft = False
                isUp = True
                isDown= False
                isRight=False
            
            
            if row > 0 and isUp:
                for i in range(row):
                    # print("isUp: ", curr_index, row, col)
                    curr_index[0] -= 1
                    ans.append(matrix[curr_index[0]][curr_index[1]])
                col -= 1
                isRight = True
                isup = False
                isLeft = False
                isDown= False
        return ans
