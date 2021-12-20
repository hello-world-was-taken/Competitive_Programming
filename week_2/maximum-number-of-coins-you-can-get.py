#QUESTION
#https://leetcode.com/problems/maximum-number-of-coins-you-can-get/


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        arr_len = len(piles)
        chosen = []
        count = 0
        for i in range(arr_len):
            chosen.append([piles[i], piles[-2-(i*2)], piles[-1-(i*2)]])
            count += 1
            if count == arr_len // 3:
                break
            else: 
                continue
        ans = 0
        print(chosen)
        for i in chosen:
            ans += i[1]
        return ans
