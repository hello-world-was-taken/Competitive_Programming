#QUESTION
#https://leetcode.com/problems/pancake-sorting/


class Solution:     
    def reverse_and_append(self, arr, index):
        temp = arr[:index + 1]
        temp = temp[::-1]
        temp += arr[index + 1:]
        return temp
    def pancakeSort(self, arr: List[int]) -> List[int]:
        arr_len = len(arr)
        ans = []
        curr_max = -1
        curr_max_index = -1
        for i in range(arr_len - 1, -1, -1):
            in_loop = False
            j = 0
            while j < (i + 1):
                if arr[j] > curr_max:
                    curr_max = arr[j]
                    curr_max_index = j
                    in_loop = True
                j += 1
            curr_max = -1
            if(not(curr_max_index == i)):
                arr = self.reverse_and_append(arr, curr_max_index)
                ans.append(curr_max_index + 1)
                temp = arr[: i+1]
                temp = temp[::-1]
                temp += arr[i + 1:]
                arr = temp
                ans.append(i + 1)
        return ans
