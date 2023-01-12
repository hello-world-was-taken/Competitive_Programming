# https://leetcode.com/problems/unique-paths-iii/

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        num_obstacles = 0
        free_path = 0
        starting_cell = None
        ending_cell = None
        in_bound = lambda row, col: 0<=row<len(grid) and 0<=col<len(grid[0])
        DIR = [(1,0), (0,1), (-1,0), (0,-1)]
        self.final_ans = 0
        self.visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == -1:
                    num_obstacles += 1
                elif grid[i][j] == 1:
                    starting_cell = (i,j)
                elif grid[i][j] == 2:
                    ending_cell = (i,j)
                else:
                    free_path += 1
                    
        def dfs(cell, path):
            if cell == ending_cell and path == free_path + 1:
                self.final_ans += 1
            elif cell == ending_cell:
                return
                
            for d in DIR:
                n_cell = (cell[0] + d[0], cell[1] + d[1])
                if in_bound(n_cell[0], n_cell[1]) and n_cell not in self.visited and grid[n_cell[0]][n_cell[1]] != -1:
                    self.visited.add(n_cell)
                    dfs(n_cell, path + 1)
                    self.visited.remove(n_cell)
        self.visited.add(starting_cell)
        dfs(starting_cell, 0)
        return self.final_ans
                    
        
