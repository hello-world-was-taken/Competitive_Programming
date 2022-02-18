#https://leetcode.com/problems/swap-nodes-in-pairs/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        tempHead = head
        tempHeadNext = tempHead.next
        if tempHeadNext != None:
            tempHeadNextNext = tempHeadNext.next
        
            tempHead.next = tempHeadNextNext
            tempHeadNext.next = tempHead
            head = tempHeadNext

            curr = tempHeadNextNext
        else:
            return head
        
        while curr != None:
            currNext = curr.next
            if currNext != None:
                currNextNext = currNext.next
                tempHead.next = currNext
                currNext.next = curr
                curr.next = currNextNext
                tempHead = curr
                curr = curr.next
            else:
                return head
        return head
