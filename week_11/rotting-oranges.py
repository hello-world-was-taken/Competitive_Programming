#https://leetcode.com/problems/rotting-oranges/



class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        
        # the number of rotten oranges at the start
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    queue.append((r,c))
                    
        DIR = [(1,0), (0,1), (-1,0), (0,-1)]
        is_bound = lambda row, col: 0<=row<len(grid) and 0<=col<len(grid[0])
        visited = set()
        visited_ones = set()
        minute = 0
        
        while queue:
            size = (len(queue))
            there_was_a_change = False
            
            for i in range(size):
                cell = queue.popleft()
                if grid[cell[0]][cell[1]] == 2:
                    for d in DIR:
                        new_cell = (cell[0]+d[0], cell[1]+d[1])
                        if is_bound(new_cell[0], new_cell[1]) and grid[new_cell[0]][new_cell[1]] == 1 and new_cell not in visited:
                            grid[new_cell[0]][new_cell[1]] = 2
                            queue.append(new_cell)
                            visited.add(new_cell)
                            there_was_a_change = True
                else:
                    if grid[cell[0]][cell[1]] == 0:
                        visited.add(cell)
                    elif grid[cell[0]][cell[1]] == 1:
                        visited_ones.add(cell)
                    for d in DIR:
                        new_cell = (cell[0]+d[0], cell[1]+d[1])
                        if is_bound(new_cell[0], new_cell[1]) and new_cell not in visited and new_cell not in visited_ones:
                            queue.append(new_cell)
            if there_was_a_change:
                minute += 1
            
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        
        
        return minute
