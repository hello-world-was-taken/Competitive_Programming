#QUESTION
#https://leetcode.com/problems/find-target-indices-after-sorting-array/

def targetIndices(self, nums, target):
        arr_len = len(nums)
        
        # Find the maximum number in the given list
        maximum_num = 0
        for i in nums:
            if i > maximum_num:
                maximum_num = i
        print(maximum_num)
        
        # Count the number of times each number exits in the given list
        new_list = [0] * (maximum_num + 1)
        for i in nums:
            new_list[i] += 1
        print(new_list)
        
        # Find the cumulative to find the last index for each number
        new_list_len = len(new_list)
        for i in range(1, new_list_len):
            new_list[i] = new_list[i] + new_list[i-1]
        print(new_list)
        
        # # Find the sorted list
        sorted_list = [0] * arr_len
        for i in nums:
            last_index_for_current = new_list[i] - 1
            sorted_list[last_index_for_current] = i
            new_list[i] -= 1
        print(sorted_list)
        
        # Now to answer what the current question asks
        index_of_target = []
        for i in range(arr_len):
            if sorted_list[i] == target:
                index_of_target.append(i)
        
        return index_of_target
