#https://leetcode.com/problems/first-bad-version/


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        first = -1
        while left <= right:
            mid = sum([left, right]) // 2
            if isBadVersion(mid):
                first = mid
                right = mid - 1
            if not isBadVersion(mid):
                left = mid + 1
        return first
