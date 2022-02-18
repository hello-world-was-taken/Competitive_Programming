#https://leetcode.com/problems/palindrome-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        
        i = 0
        while i < len(arr):
            if arr[i] != arr[-(i+1)]:
                return False
            if i > len(arr)// 2:
                return True
            i += 1
        return True
