#https://leetcode.com/problems/reorder-list/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        list_node = []
        temp_head = head
        while temp_head != None:
            list_node.append(temp_head)
            temp_head = temp_head.next
            
        for i in list_node:
            i.next = None
        
        i = 0
        up_limit = len(list_node)//2 
        while i < up_limit:
            list_node[i].next = list_node[-1 - i]
            if (i + 1) < up_limit:
                list_node[-1-i].next = list_node[i+1]
            else:
                list_node[-1-i].next = None
            i += 1
        
        if len(list_node) % 2 == 1 and len(list_node) > 2:
            list_node[up_limit + 1].next = list_node[up_limit]
            list_node[up_limit].next = None
