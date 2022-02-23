#https://leetcode.com/problems/merge-k-sorted-lists/



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        arr_len = len(lists)
        heap = []
        if len(lists) == 0:
            return None
        
        for i in range(len(lists)):
            if lists[i] == None:
                continue
            heapq.heappush(heap, (lists[i].val, i))
            
        
        temp_head = head = ListNode(0)
        while len(heap) > 0:
            temp_min = heapq.heappop(heap) # what we are popping is actually a tuple
            temp_head.next = lists[temp_min[1]]
            temp_head = temp_head.next
            lists[temp_min[1]] = lists[temp_min[1]].next
            if lists[temp_min[1]] != None:
                heapq.heappush(heap, (lists[temp_min[1]].val, temp_min[1]))
        
        return head.next
