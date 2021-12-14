#QUESITION
#https://leetcode.com/problems/find-the-kth-largest-integer-in-the-array/submissions/


def kthLargestNumber(self, nums, k):
    arr_len = len(nums)
    int_nums = [0] * arr_len
    
    # Convert the strings to ints
    for i in range(arr_len):
        int_nums[i] = int(nums[i])
        
    int_nums.sort(reverse=True)
    
    # Re-iterate and copy
    for i in range(arr_len):
        nums[i] = str(int_nums[i])
    print(nums)
    
    return nums[k-1]