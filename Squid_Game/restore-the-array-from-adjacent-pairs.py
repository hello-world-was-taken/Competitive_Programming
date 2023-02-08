# https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        count = defaultdict( list )
        
        # the first and the last will always have one adjacent
        for num1, num2 in adjacentPairs:
            count[num1].append( num2 )
            count[num2].append( num1 )
        
        start_end = [ num for num in count.keys() if len(count[num]) == 1]
        start, end = start_end
        
        visited = set()
        _next = count[start][0]
        ans = [ start ]
        visited.add( start )
        
        while _next not in visited:
            ans.append( _next )
            visited.add( _next )
            
            for num in count[_next]:
                if num not in visited:
                    _next = num
        
        return ans
