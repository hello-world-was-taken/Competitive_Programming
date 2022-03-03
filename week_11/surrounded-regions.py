#https://leetcode.com/problems/surrounded-regions/



class Solution:
    
    def capture(self, curr_index):
        
        for d in self.DIR:
            nri, nci = d[0]+curr_index[0], d[1]+curr_index[1]
            
            if self.is_inbound(nri, nci) and ((nri, nci) not in self.visited) and self.board[nri][nci] == "O":
                self.visited.add((nri, nci))
                self.temp_valid.append((nri, nci))
                self.capture((nri, nci))
            elif not self.is_inbound(nri, nci):
                self.out_of_bound = True
    
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.DIR = [(1,0), (0,1), (-1,0), (0,-1)]
        self.is_inbound = lambda row, col: 0<=row<len(board) and 0<=col<len(board[0])
        self.valid_o = []
        self.visited = set()
        self.board = board
        self.temp_valid = []
        self.out_of_bound = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.board[i][j] == "O" and (i,j) not in self.visited:
                    self.temp_valid.append((i,j))
                    self.visited.add((i, j))
                    self.capture((i, j))
                    if not self.out_of_bound:
                        self.valid_o.append(self.temp_valid)
                    self.temp_valid = []
                    self.out_of_bound = False
                
        for row in self.valid_o:
            for tup in row:
                self.board[tup[0]][tup[1]] = "X"
        
