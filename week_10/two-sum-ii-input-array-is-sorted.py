#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        arr_len = len(numbers)
        i = 0
        j = arr_len - 1
        
        my_target = -10000
        while i < j:
            temp_sum = numbers[i] + numbers[j]
            if temp_sum > target:
                j -= 1
            elif temp_sum < target:
                i += 1
            else:
                return [i+1, j+1]
