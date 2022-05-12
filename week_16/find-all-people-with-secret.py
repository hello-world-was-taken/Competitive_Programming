# https://leetcode.com/problems/find-all-people-with-secret/



class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        g = defaultdict(list)

        for meeting in meetings:
            g[meeting[0]].append((meeting[2], meeting[1]))
            g[meeting[1]].append((meeting[2], meeting[0]))
        # print(g)
            
        heap = []
        heappush(heap, (0, 0)) # zero has a connection with zero in the begining
        heappush(heap, (0, firstPerson)) # the same with the firstPerson
        visited = set()
        
        while len(heap):
            curr = heappop(heap)
            
            if curr[1] in visited:
                continue
                
            visited.add(curr[1])
            
            for edge in g[curr[1]]:
                
                if edge[1] in visited:
                    continue
                
                if edge[0] >= curr[0]:
                    heappush(heap, edge)
                    
        return [node for node in visited]
            
