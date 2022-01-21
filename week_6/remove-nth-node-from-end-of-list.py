#https://leetcode.com/problems/remove-nth-node-from-end-of-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        temp_head = head
        while temp_head != None:
            count += 1
            temp_head = temp_head.next
        
        before_removed = head
        
        # check if the count equals the values whic is an edge case.
        if n == count:
            return head.next
        
        go_to = count - n
        
        while go_to > 1:
            before_removed = before_removed.next
            go_to -= 1
        
        before_removed.next = before_removed.next.next
        return head
