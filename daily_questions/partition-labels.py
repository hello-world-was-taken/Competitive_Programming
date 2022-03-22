# https://leetcode.com/problems/partition-labels/



class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic = defaultdict(int)
        unique = set()
        count = 0
        ans = []
        total_negated_till_now = 0
        
        
        for i in s:
            dic[i] += 1
        
        for i in s:
            unique.add(i)
            dic[i] -= 1
            total_negated_till_now += 1

            for j in list(unique):

                if dic[j] == 0:
                    # print("count: ", j, " ", dic[j])
                    count += 1
            if count == len(unique):
                ans.append(total_negated_till_now)
                unique = set()
                total_negated_till_now = 0
            count = 0
        return ans   
