# https://leetcode.com/problems/min-cost-to-connect-all-points/



class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        g = defaultdict(list)
        for i in range(len(points)):
            for j in range(len(points)):
                if i != j:
                    g[(points[i][0], points[i][1])].append((abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]), (points[j][0], points[j][1])))
                    
        visited = set()
        heap = []
        heap.append((0, (points[0][0], points[0][1])))
        cost = 0
        
        while len(heap) and len(visited) < len(points):
            curr = heappop(heap)
            
            if curr[1] not in visited:
                visited.add(curr[1])
                cost += curr[0]
                
                for point in g[curr[1]]:
                    heappush(heap, point)
        
        return cost
            
