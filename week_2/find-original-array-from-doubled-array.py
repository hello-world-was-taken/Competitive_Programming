#QUESTION
#https://leetcode.com/problems/find-original-array-from-doubled-array/

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        arr_len = len(changed)
        ans = []
        if (arr_len % 2 != 0):
            return []
        
        dic_count = Counter(changed)
        
        for i in changed:
            if i == 0 and dic_count[i] >= 2:
                dic_count[i] -= 2
                ans.append(i)
            elif i > 0 and dic_count[i] and dic_count[i*2]:
                dic_count[i] -= 1
                dic_count[i*2] -= 1
                ans.append(i)
        
        return ans if len(ans) == (len(changed) // 2) else []
