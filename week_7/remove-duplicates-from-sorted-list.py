#https://leetcode.com/problems/remove-duplicates-from-sorted-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp_head = head
        while temp_head != None and temp_head.next != None:
            if temp_head.val == temp_head.next.val:
                temp_head.next = temp_head.next.next
            else:
                temp_head = temp_head.next
                
        return head
