#QUESTION
#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

#     def smallerNumbersThanCurrent(self, nums):    #MORE EFFICIENT MEMORY WISE
#         arr_len = len(nums)
#         newList = [0] * arr_len
#         for i in range(arr_len):
#             count = 0
#             for j in range(arr_len):            
#                 if(nums[i] > nums[j]):
#                     count += 1
#             newList[i] = count
            
#         return newList

    def smallerNumbersThanCurrent(self, nums):        #MORE EFFICIENT TIME WISE
        
        # find the maximum number in the array
        arr_len = len(nums)
        maxi = nums[0]
        for i in range(arr_len):
            if nums[i] > maxi:
                maxi = nums[i]
        
        newList = [0] * (maxi + 1) # the 1 is because indexing starts at zero
        newList2 = [0] * (maxi + 1)
        for i in nums:
            newList[i] += 1
            newList2[i] += 1
        
        print(newList2)
        
        #finding the cumulative. To find last index it will be at.
        newList_len = len(newList)
        for i in range(1, newList_len):
            newList[i] = newList[i] + newList[i-1]
            
        print(newList)
        
        # creating a new list to store the final result
        # final_list = [0] * arr_len
        # for i in nums:
        #     last_index = newList[i] - 1
        #     final_list[last_index] = i
        #     newList[i] -= 1
            
        # print(final_list)
        
        less_nums = [0] * arr_len
        for i in range(arr_len):
            less_nums[i] = newList[nums[i]] - newList2[nums[i]]
            
        return less_nums
