#https://leetcode.com/problems/sort-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def compare(item1):
        return item1.val
        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        list_node = []
        while head != None:
            list_node.append(head)
            head = head.next
        
        list_node.sort(key=compare)
        
        
        for i in list_node:
            i.next = None
        
        i = 0
        while i < (len(list_node) - 1):
            list_node[i].next = list_node[i+1]
            i += 1
            
        return list_node[0] if len(list_node) > 0 else None
        
