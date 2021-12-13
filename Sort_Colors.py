#QUESTION
#https://leetcode.com/problems/sort-colors/submissions/

def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # # Find the maximum number IS NOT NEEDED AS IT WILL ALWAYS BE 2
        # maximum_num = 0
        # for i in nums:
        #     if i > maximum_num:
        #         maximum_num = i
        # print(maximum_num)
        
        # Find the count for 0, 1 and 2
        arr_len = len(nums)
        cummulative_arr = [0] * (3)
        for i in nums:
            cummulative_arr[i] += 1
        print(cummulative_arr)
        
        # Find the cummulative for each index
        for i in range(1, 3):
            cummulative_arr[i] = cummulative_arr[i] + cummulative_arr[i-1]
        print(cummulative_arr)
        
        # Sort the array
        sorted_list = [0] * arr_len
        for i in nums:
            last_index_for_current = cummulative_arr[i] - 1
            sorted_list[last_index_for_current] = i
            cummulative_arr[i] -= 1
        # nums = sorted_list
        print(nums)
        
        # As per the questions request we simply iterate and update the values of nums
        for i in range(arr_len):
            nums[i] = sorted_list[i]
