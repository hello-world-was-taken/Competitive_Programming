def simple_compare(self, num1, num2):
    num1 = str(num1)
    num2 = str(num2)
    
    first_append = num1 + num2
    first_append = int(first_append)
    
    second_append = num2 + num1
    second_append = int(second_append)
    
    if first_append > second_append:
        return True
    return False


# Change number list to string list
def list_string(self, li):
    li_len = len(li)
    ans = [0] * li_len
    for i in range(li_len):
        ans[i] = str(li[i])
    return ans

def append_to_string(self, li):
    ans = ""
    for i in li:
        ans += i
    return ans

def largestNumber(self, nums: List[int]) -> str:
    arr_len = len(nums)
    
    if sum(nums) == 0:
        return "0"
    
    for i in range(arr_len):
        for j in range(arr_len-1-i):
            swap = self.simple_compare(nums[j], nums[j+1])
            if(swap):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    nums.reverse()
    ans_string = []
    ans_string = self.list_string(nums)
    return (self.append_to_string(ans_string))