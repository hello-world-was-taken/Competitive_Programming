#https://leetcode.com/problems/next-greater-node-in-linked-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        temp_head = head
        count = 0
        while temp_head != None:
            count += 1
            temp_head = temp_head.next
        
        ans_arr = [0]*count
        temp_head = head
        min_stack = []
        pseudo_index = 0
        while temp_head != None:
            if len(min_stack) == 0:
                min_stack.append((temp_head.val,pseudo_index))
                pseudo_index += 1
                temp_head = temp_head.next
                continue
            if temp_head.val <= min_stack[-1][0]:
                min_stack.append((temp_head.val,pseudo_index))
                pseudo_index += 1
                temp_head = temp_head.next
                continue
            else:
                while len(min_stack) > 0 and min_stack[-1][0] < temp_head.val:
                    popped = min_stack.pop()
                    ans_arr[popped[1]] = temp_head.val
                min_stack.append((temp_head.val, pseudo_index))
                pseudo_index += 1
                temp_head = temp_head.next
        return ans_arr
