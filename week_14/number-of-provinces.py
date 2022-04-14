#https://leetcode.com/problems/number-of-provinces/



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parents = [i for i in range(len(isConnected))]
        def path_compress(i):
            if parents[i] == i:
                return i
            p = path_compress(parents[i])
            parents[i] = p
            return p
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    parents[path_compress(i)] = path_compress(j)
                    
        for i in range(len(isConnected)):
            path_compress(i)
            
        return len(set(parents))
        
