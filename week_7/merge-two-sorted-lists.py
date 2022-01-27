#https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans_list = ListNode()
        final_ans = ans_list
        if list1 == None and list2 == None:
            return None
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                ans_list.val = list1.val
                list1 = list1.next
            else:
                ans_list.val = list2.val
                list2 = list2.next
                
            new_node = ListNode()
            ans_list.next = new_node
            ans_list = ans_list.next
        
        if list1 != None:
            ans_list.val = list1.val
            ans_list.next = list1.next
        if list2 != None:
            ans_list.val = list2.val
            ans_list.next = list2.next
        return final_ans
