#https://leetcode.com/problems/number-of-provinces/


class Solution:
    def find_relation(self, key):
        for list_node in self.dic[key]:
            if len(self.dic[key]) and list_node not in self.visited:
                self.visited.add(key)
                self.find_relation(list_node)
    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.isConnected = isConnected
        self.visited = set()
        self.province_count = 0
        self.dic = {}
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    if self.dic.get(i):
                        self.dic[i].append(j)
                    else:
                        self.dic[i] = []
                        self.dic[i].append(j)
        
        for key in list(self.dic.keys()):
            for list_node in self.dic[key]:
                if len(self.dic[key]) and list_node not in self.visited:
                    self.find_relation(list_node)
                    self.province_count += 1
        return self.province_count
