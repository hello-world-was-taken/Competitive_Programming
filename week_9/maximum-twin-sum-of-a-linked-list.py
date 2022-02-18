#https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def linked_reverse(self, temp_head):
        prev = None
        curr = temp_head
        if temp_head.next == None:
            return temp_head
        while curr != None:
            curr_next = curr.next
            if curr_next == None:
                curr.next = prev
                return curr
            next_next = curr_next.next
            
            curr_next.next = curr
            curr.next = prev
            
            curr = next_next
            prev = curr_next
        return prev
        
        
    
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp_head = head
        count = 0
        while temp_head != None:
            temp_head = temp_head.next
            count += 1
        
        second_half = None
        temp_head = head
        i = 0
        while i < count//2:
            temp_head = temp_head.next
            i += 1
        second_half = self.linked_reverse(temp_head)
        
        maxi = 0
        temp_head = head
        while second_half != None:
            maxi = max(maxi, (temp_head.val + second_half.val))
            temp_head =temp_head.next
            second_half = second_half.next
            
        return maxi
