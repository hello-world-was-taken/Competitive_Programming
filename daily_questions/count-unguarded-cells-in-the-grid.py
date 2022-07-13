# https://leetcode.com/problems/count-unguarded-cells-in-the-grid/



class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        guards_set = set()
        walls_set = set()
        self.guarded = set()
        DIR = [(1,0), (0,1), (-1,0), (0,-1)]
        is_bound = lambda a, b: 0 <= a < m and 0 <= b < n
        self.visited = set()
        
        def travel(cell, d):
            if is_bound(cell[0], cell[1]) and cell not in guards_set and cell not in walls_set:
                if (cell[0], cell[1]) not in self.visited:
                    self.visited.add((cell[0], cell[1]))
                travel((cell[0] + d[0], cell[1] + d[1]), d)
            return
            
        
        for guard in guards:
            guards_set.add((guard[0], guard[1]))
        for wall in walls:
            walls_set.add((wall[0], wall[1]))
        
        for guard in guards:
            for d in DIR:
                travel((guard[0] + d[0], guard[1] + d[1]), d)
        # print("visited: ", len(self.visited))
        return (m*n) - (len(self.visited) + len(guards) + len(walls))
            
