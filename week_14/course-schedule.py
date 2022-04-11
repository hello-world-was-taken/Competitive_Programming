# https://leetcode.com/problems/course-schedule/



class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_rep = defaultdict(list)
        self.visited = set()
        for i in prerequisites:
            adj_rep[i[0]].append(i[1])
        
        def dfs(node):
            if node in self.visited:
                return False
            
            self.visited.add(node)
            
            for i in adj_rep[node]:
                if not dfs(i): 
                    return False
            
            self.visited.remove(node)   
            adj_rep[node] = []
            
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
    
