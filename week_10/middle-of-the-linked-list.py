#https://leetcode.com/problems/middle-of-the-linked-list/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        turtle = head
        hare = head
        
        while turtle and turtle.next:
            hare = hare.next
            turtle = turtle.next.next
        return hare
#         count = []
#         while head != None:
#             count.append(head)
#             head = head.next
        
#         return count[len(count)//2]
        
