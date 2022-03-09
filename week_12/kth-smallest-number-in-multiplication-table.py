#https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/



class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # for each number in our value, which we get through our binary search,
        # we find the number of numbers which are less than that.
        # if the amount of numbers we find less than that equal 'k' we have found our solution.
        
        def count_less_numbers(num):
            count = 0
            for i in range(1, n+1):
                count += min(num//i, m) # here num/n will give us the number of elements with less value than the current num
            return count
        
        
        left = 1
        right = m * n
        
        while left < right:
            mid = (left + right)//2

            if count_less_numbers(mid) < k:
                left = mid +1
            else:
                right = mid
        
        return left
