# https://leetcode.com/problems/max-area-of-island/



class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def path_compress(node):
            if parents[node] == node:
                return node
            parents[node] = path_compress(parents[node])
            return parents[node]
        
        
        parents = {}
        is_bound = lambda r,c: 0 <= r < len(grid) and 0 <= c < len(grid[0])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    parents[(i,j)] = (i, j)

                    
        
        DIR = [(1,0), (0,1), (-1,0), (0,-1)]
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for d in DIR:
                    neigh = (i+d[0], j+d[1])
                    if grid[i][j] == 1 and is_bound(neigh[0], neigh[1]) and grid[neigh[0]][neigh[1]] == 1: 
                            parents[path_compress((i, j))] = parents[path_compress((neigh[0], neigh[1]))]

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    path_compress((i,j))

        c = Counter(parents.values())
        
        return max(c.values()) if c.values() else 0
