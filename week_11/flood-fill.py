#https://leetcode.com/problems/flood-fill/


class Solution:
    # def __init__(self):
        # self.visited = set()
        
    def change_color(self, index):
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        
        for direction in directions:
            new_row_index, new_col_index = index[0]+direction[0], index[1]+direction[1]
            if (new_row_index < self.row_limit) and (new_col_index < self.col_limit) and (new_row_index > -1) and (new_col_index > -1):
                if self.image[new_row_index][new_col_index] == self.old_color:
                    self.image[new_row_index][new_col_index] = self.new_color
                    self.change_color([new_row_index, new_col_index])
        return
    
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if newColor == image[sr][sc]:
            return image
        
        self.old_color = image[sr][sc]
        self.new_color = newColor
        image[sr][sc] = self.new_color
        self.row_limit = len(image)
        self.col_limit = len(image[0])
        self.image = image
        self.change_color([sr, sc])
        
        return image
