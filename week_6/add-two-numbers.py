#https://leetcode.com/problems/add-two-numbers/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # converts a given linked list to a number
    def toNumber(self, head):
        total = 0
        while head != None:
            total += head.val
            head = head.next
            if head != None:
                total *= 10
        return total
    
    # converts a given number's digits to a linked list
    def toLinkedList(self, num):
        head = ListNode()
        g_head = head
        head.val = num % 10
        head.next = None
        num -= num%10
        num //=10
        while num > 0:
            temp = ListNode()
            temp.val = num%10
            temp.next = None
            num -= num%10
            num //= 10
            head.next = temp
            head = head.next
        return g_head
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr_1 = l1
        prev_1 = None
        next_node_1 = curr_1.next
        
        # reverse l1    WE COULD CREATE A FUNCTION THAT REVERSES THE LINKED LISTS TOO.
        while next_node_1 != None:
            next_node_1 = curr_1.next
            curr_1.next = prev_1
            prev_1 = curr_1
            if next_node_1 != None:
                curr_1 = next_node_1
        number_1 = self.toNumber(curr_1)
        curr_2 = l2
        prev_2 = None
        next_node_2 = curr_2.next
        
        # reverse l2
        while next_node_2 != None:
            next_node_2 = curr_2.next
            curr_2.next = prev_2
            prev_2 = curr_2
            if next_node_2 != None:
                curr_2 = next_node_2
        
        number_2 = self.toNumber(curr_2)
        
        result = number_1 + number_2
        return self.toLinkedList(result)
