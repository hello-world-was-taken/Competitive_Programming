#https://leetcode.com/problems/minesweeper/



class Solution:
    def dummy(self, curr_index):
        mine = 0
        for d in self.DIR:
            nri, nci = d[0]+curr_index[0], d[1]+curr_index[1]
            if self.is_bound(nri, nci) and (nri,nci) not in self.visited:
                if self.board[nri][nci] == 'M':
                    mine += 1
        return mine
    
    def adj_mines(self, curr_index):
        mine_count = 0
        temp = []
        for d in self.DIR:
            nri, nci = d[0]+curr_index[0], d[1]+curr_index[1]
            if self.is_bound(nri, nci) and (nri,nci) not in self.visited:
                if self.board[nri][nci] == 'M':
                    mine_count += 1
                else:
                    temp.append((nri, nci))
                    self.visited.add((nri, nci))
        if mine_count == 0:
            self.change_to_B(curr_index)
            if len(temp):
                for i in temp:
                    self.adj_mines(i)
        else:
            self.board[curr_index[0]][curr_index[1]] = str(mine_count)
            for i in temp:
                self.visited.remove(i)
            
        return
    
    def change_to_B(self, curr_index):
        mine_count = 0
        for d in self.DIR:
            nri, nci = d[0]+curr_index[0], d[1]+curr_index[1]
            if self.is_bound(nri, nci) and self.board[nri][nci] == 'E':
                self.board[nri][nci] = 'B'
    
    def mine_sweeper(self, click):
        self.adj_mines((click[0], click[1]))
    
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.is_bound = lambda row,col: 0<=row<len(board) and 0<=col<len(board[0])
        self.DIR = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        self.board = board
        self.visited = set()
        
        if self.board[click[0]][click[1]] == 'M':
            self.board[click[0]][click[1]] = 'X'
            return self.board
        else:
            self.board[click[0]][click[1]] = self.dummy(click) if self.dummy(click) > 0 else 'B'
            self.mine_sweeper(click)
            
        
        return self.board
