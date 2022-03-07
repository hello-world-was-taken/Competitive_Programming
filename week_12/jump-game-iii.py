#https://leetcode.com/problems/jump-game-iii/



class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        is_bound = lambda index: 0 <= index < len(arr)
        visited = set()
        self.found_zero_at = None
        def find_zero(index):
            visited.add(index)
            new_indices = [index + arr[index], index - arr[index]]
            
            for new_index in new_indices:
                if is_bound(new_index) and new_index not in visited:
                    if arr[new_index] == 0:
                        self.found_zero_at = new_index
                        return
                    find_zero(new_index)
        if arr[start] == 0:
            return True
        
        find_zero(start)
        if self.found_zero_at != None:
            return True
        return False
            
