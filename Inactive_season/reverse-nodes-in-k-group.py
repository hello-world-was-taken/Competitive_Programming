# https://leetcode.com/problems/reverse-nodes-in-k-group/

class Solution:
    
    def reverseKGroup(self, head, k):
        current = head
        while current != None:
            current = self.switcher(current, k, k//2)
        
        return head
        
        
    def switcher(self, head, k, loop):
        if loop == 0:
            return
        current = head
        first = current
        kth = None
        count = 1
        while count <= k:
            if current == None:
                return
            if count == 1:
                first = current
            elif count == k:
                kth = current
                temp = first.val
                first.val = kth.val
                kth.val = temp
                # count = 0
            count += 1
            current = current.next
        loop -= 1
        self.switcher(first.next, k-2, loop)
        return kth.next
