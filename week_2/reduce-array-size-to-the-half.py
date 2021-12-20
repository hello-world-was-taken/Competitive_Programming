#QUESTION
#https://leetcode.com/problems/reduce-array-size-to-the-half/


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        arr_len = len(arr)
        # arr.sort()
        dic_count = Counter(arr)
        print(dic_count)
        count_sorted = list(dic_count.values())
        count_sorted.sort(reverse=True)
        print(count_sorted)
        ans = 0
        for i in range(len(count_sorted)):
            ans += count_sorted[i]
            if ans >= (arr_len//2):
                return i + 1
        
