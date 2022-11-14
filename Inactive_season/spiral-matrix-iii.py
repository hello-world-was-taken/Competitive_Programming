# https://leetcode.com/problems/spiral-matrix-iii/

class Solution:
    
    def is_inbound(self, row, col, row_bound, col_bound):
        return 0 <= row < row_bound and 0 <= col < col_bound
    
    
    '''
    Move our index in the direction given for the number of steps provided.
    '''
    def move(self , current_start , direction , visited , steps, row_bound, col_bound):
        row, col = current_start[0] , current_start[1] 
        
        while steps > 0:
            row, col = row + direction[0], col + direction[1]  # updating our row and col with each move
            
            bound = self.is_inbound(row, col, row_bound, col_bound)
            if bound:
                visited.append((row, col))
            steps -= 1
        
        return row , col
            
        
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        
        visited = [(rStart, cStart)]
        
                    # east,  south,  west,  north
        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        west, east = (0, -1), (0, 1)         # a special directions where we will need to increase our steps by 1
        
        current_visited_length = len(visited)
        current_start = (rStart, cStart)
        steps = 0
        
        while current_visited_length < (rows * cols):
            for direction in directions:
                if direction == west or direction == east:
                    steps += 1
                current_start = self.move(current_start, direction, visited, steps, rows, cols)
          
            current_visited_length = len(visited)
                  
        return visited
