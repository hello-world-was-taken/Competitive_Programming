# https://leetcode.com/problems/plus-one/


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if int(digits[i]) == 9:
                digits[i] = '0'
            else:
                digits[i] = str(int(digits[i]) + 1)
                carry = 0
                break
        
        if carry == 1:
            return [1] + list(map(int, digits))
        return list(map(int, digits))
