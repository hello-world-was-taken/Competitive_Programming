# https://leetcode.com/problems/course-schedule-ii/



class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dep_count = [0 for i in range(numCourses)]
        adj_map = {i : [] for i in range(numCourses)}
        
        for cour , pre in prerequisites:
            dep_count[cour] += 1
            adj_map[pre].append(cour)
        
        queue = deque(filter(lambda idx : dep_count[idx] == 0, range(numCourses)))
        ans = []
        
        while queue:
            course = queue.popleft()
            ans.append(course)
            
            for i in adj_map[course]:
                dep_count[i] -= 1
                if dep_count[i] == 0:
                    queue.append(i)
        
        return [] if len(ans) != numCourses else ans
