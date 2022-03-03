#https://leetcode.com/problems/number-of-enclaves/
#An exact replica of surounded-regions. I just copied and pasted that code and well it worked!



class Solution:
    def capture(self, curr_index):
        
        for d in self.DIR:
            nri, nci = d[0]+curr_index[0], d[1]+curr_index[1]
            
            if self.is_inbound(nri, nci) and ((nri, nci) not in self.visited) and self.grid[nri][nci] == 1:
                self.visited.add((nri, nci))
                self.temp_valid.append((nri, nci))
                self.capture((nri, nci))
            elif not self.is_inbound(nri, nci):
                self.out_of_bound = True
    
    def numEnclaves(self, grid: List[List[int]]) -> int:
        self.DIR = [(1,0), (0,1), (-1,0), (0,-1)]
        self.is_inbound = lambda row, col: 0<=row<len(grid) and 0<=col<len(grid[0])
        self.valid_o = []
        self.visited = set()
        self.grid = grid
        self.temp_valid = []
        self.out_of_bound = False
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.grid[i][j] == 1 and (i,j) not in self.visited:
                    self.temp_valid.append((i,j))
                    self.visited.add((i, j))
                    self.capture((i, j))
                    if not self.out_of_bound:
                        self.valid_o.append(self.temp_valid)
                    self.temp_valid = []
                    self.out_of_bound = False
        print(self.valid_o)
        count = 0
        for row in self.valid_o:
            for tup in row:
                count += 1
        return count
