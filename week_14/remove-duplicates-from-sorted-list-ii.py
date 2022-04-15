# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            prev = head
            _next = head.next
            
            # handles when the first values are equal
            while prev and _next and prev.val == _next.val:
                prev_prev = prev
                while prev and prev_prev.val == prev.val:
                    prev_prev = prev
                    prev = prev.next

                if prev:
                    _next = prev.next
                else:
                    _next = None
            
            head = prev
            if prev:
                _next = prev.next
            while prev and _next:
                d_found = False
                if _next.next:
                    if _next.next.val == _next.val:
                        t_prev = _next
                        while _next and _next.val == t_prev.val:
                            d_found = True
                            _next = _next.next

                        prev.next = _next
                    if not d_found:
                        prev = _next
                        _next = prev.next
                        d_found = False
                    else:
                        pass
                else:
                    break
            
        return head
                        
