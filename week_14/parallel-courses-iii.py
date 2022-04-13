# https://leetcode.com/problems/parallel-courses-iii/



class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        in_degree = [0 for i in range(n+1)]
        graph = defaultdict(list)
        
        for pre, crs in relations:
            graph[pre].append(crs)
            in_degree[crs] += 1
        
        queue = deque()
        dist = [0] * (n)
        
        for i,v in enumerate(in_degree):
            
            if v == 0:
                queue.append(i)
                dist[i-1] = time[i-1] # since the time is 0 indexed
                
        while queue:
            pre = queue.popleft()
            
            for d in graph[pre]:
                in_degree[d] -= 1
                dist[d-1] = max(dist[pre-1]+time[d-1], dist[d-1])
                
                if in_degree[d] == 0:
                    queue.append(d)
                    
        return max(dist)
