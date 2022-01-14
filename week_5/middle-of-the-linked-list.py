#QUESTION
#https://leetcode.com/problems/middle-of-the-linked-list/

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # OPTIMIZED IMPLEMENTATION
        turtle = head
        hare = head
        
        while turtle and turtle.next:
            hare = hare.next
            turtle = turtle.next.next
        return hare
      # KINDA LIKE BRUTE FORCE IMPLEMENTATION
#         count = []
#         while head != None:
#             count.append(head)
#             head = head.next
        
#         return count[len(count)//2]
        
