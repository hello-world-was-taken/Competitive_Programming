class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        arr_len = len(nums)
        nums.sort(reverse=True)
        maxi = 0
        
        i = 0
        j = 0
        
        while(j < arr_len):
            if (nums[i] - nums[j] <= k):
                k -= nums[i] - nums[j]
                maxi = max(maxi, j - i + 1)
                j += 1
            else:
                to_be_added = j - i - 1
                k += (nums[i] - nums[i+1]) * to_be_added
                i += 1
        return maxi
