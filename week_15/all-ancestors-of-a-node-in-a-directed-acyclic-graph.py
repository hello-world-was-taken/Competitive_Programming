# https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/



class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_map = defaultdict(set)
        indegree = [0 for i in range(n)]
        ans = [set() for i in range(n)]
        
        for val, dep in edges:
            indegree[dep] += 1
            adj_map[val].add(dep)

        queue = deque(filter(lambda x: indegree[x] == 0, range(len(indegree))))

        while queue:
            curr = queue.popleft()
            
            for dep in adj_map[curr]:
                indegree[dep] -= 1
                ans[dep].add(curr)
                ans[dep].update(ans[curr])
                
                if indegree[dep] == 0:
                    queue.append(dep)
          
        for i in range(len(ans)):
            ans[i] = list(sorted(ans[i]))
                    
        return ans
