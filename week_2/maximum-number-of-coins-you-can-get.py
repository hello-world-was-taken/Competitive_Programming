#QUESTION
#https://leetcode.com/problems/maximum-number-of-coins-you-can-get/


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        arr_len = len(piles)
        count = 0
        ans = 0
        for i in range(arr_len):
            ans += piles[-2-(i*2)]
            count += 1
            if count == arr_len // 3:
                break
            else: 
                continue
        return ans
