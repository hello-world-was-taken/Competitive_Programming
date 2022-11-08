#  https://leetcode.com/problems/single-number-iii/


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        candidate = 0
        for num in nums:
            candidate = candidate ^ num
        random_on_bit = 0
        
        for i in range(32):
            if candidate & (1 << i):
                random_on_bit = i
                break
        
        res = [0, 0]
        for num in nums:
            if num & (1 << random_on_bit) == 0:
                res[0] = res[0] ^ num
            else:
                res[1] = res[1] ^ num

        return res
