# https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/

from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, cost in roads:
            graph[u].append( (v, cost) )
            graph[v].append( (u, cost) )
            
        visited = set()
        queue = deque( [(1, float("inf"))] )
        score = float("inf")
        
        while queue:
            node, cost = queue.popleft()
            score = min(score, cost)
            
            if node not in visited:
                visited.add( node )
                for ngh, nc in graph[node]:
                    queue.append( (ngh, nc) )
                    
        return score
