#https://leetcode.com/problems/jump-game-iv/



class Solution:
    def minJumps(self, arr: List[int]) -> int:
        is_bound = lambda index: 0<= index <len(arr)
        dic = defaultdict(list)
        visited = set()
        
        for index, value in enumerate(arr):
            dic[value].append(index)

        
        queue = deque()
        queue.append((0, 0))
        while queue:
            idx , level = queue.popleft()
            visited.add(idx)
            
            if idx == len(arr) - 1:
                return level
            
            # creating our relation for the current index
            if is_bound(idx -1) and (idx -1) not in visited:
                visited.add(idx -1)
                queue.append((idx -1, level +1))
            
            if is_bound(idx +1) and (idx +1) not in visited:
                visited.add(idx +1)
                queue.append((idx +1, level +1))
                
            for i in dic[arr[idx]]:
                if i not in visited:
                    visited.add(i)
                    queue.append((i,level +1))
            
            dic[arr[idx]] = []
