#https://leetcode.com/problems/search-a-2d-matrix/


class Solution:
    def bs(self, row, target):
        left = 0
        right = len(row) -1
        while left <= right:
            mid = sum([left, right])//2
            if row[mid] > target:
                right =mid - 1
            elif row[mid] < target:
                left = mid + 1
            else:
                return True
        return False
            
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0
        bottom = len(matrix) - 1
        best_row_index = None
        while top <= bottom:
            mid = sum([top, bottom])//2
            if target >= matrix[mid][0]:
                best_row_index = mid
                top = mid + 1
            else:
                bottom = mid - 1
        row = best_row_index
        return self.bs(matrix[row], target) if row != None else False
