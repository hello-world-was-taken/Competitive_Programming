#https://leetcode.com/problems/max-area-of-island/



class Solution:
    def find_island(self, curr_index):
        for d in self.DIR:
            nri, nci = d[0]+curr_index[0], d[1]+curr_index[1]
            if self.is_inbound(nri, nci) and self.grid[nri][nci] == 1 and ((nri, nci)) not in self.visited:
                self.visited.add((nri, nci))
                self.curr_max += 1
                self.find_island((nri, nci))
                
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.DIR = [(1,0), (0,1), (-1,0), (0,-1)]
        self.is_inbound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[0])
        self.grid = grid
        self.visited = set()
        self.max_island = 0
        self.curr_max = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] not in self.visited and grid[row][col] == 1:
                    self.curr_max += 1
                    self.visited.add((row, col))
                    self.find_island((row, col))
                    self.max_island = max(self.curr_max, self.max_island)
                    self.curr_max = 0
                    
        return self.max_island
