#https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        negative = 0
        left_most_negative = None
        for row in grid:
            left = 0
            right = len(row) - 1
            
            while left <= right:
                mid = sum([left, right])//2
                # print(mid, len(row), row)
                if row[mid] < 0:
                    left_most_negative = mid
                    right = mid - 1
                elif row[mid] >= 0:
                    left = mid + 1
            if left_most_negative != None:
                negative += len(row) - (left_most_negative)
        return negative
