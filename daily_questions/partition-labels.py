# https://leetcode.com/problems/partition-labels/



class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict(int)
        ans = []
        
        for i,v in enumerate(s):
            dic[v] = i

        curr_max = -1
        sub_str_count = 0
        
        for index, value in enumerate(s):
            sub_str_count += 1
            curr_max = max(dic[value], curr_max)
            if index == curr_max:
                ans.append(sub_str_count)
                sub_str_count = 0

        return ans   
