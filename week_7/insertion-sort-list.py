#https://leetcode.com/problems/insertion-sort-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_list = ListNode()
        ans = new_list
        i = 0
        temp_head = head
        mini = temp_head.val
        mini_prev = temp_head
        curr_mini_prev = head
        slow_head = head
        # count = 1000000000000000000000
        
        # while temp_head != None:
        #     count += 1
        #     temp_head = temp_head.next
        # print(count)
        
        
        ans_list = ListNode()
        answer = ans_list
        while head != None:
            min_val = head.val
            min_prev = head
            curr_prev = head
            temp_head = head
            while temp_head != None:
                if temp_head.val < min_val:
                    min_val = temp_head.val
                    min_prev = curr_prev
                curr_prev = temp_head
                temp_head = temp_head.next
            
            # if min_prev = head:
            #     head = head.next
            if min_prev.next != None:
                if min_val== head.val:
                    # print("Gotcha")
                    # print("head first: ", head)
                    head = head.next
                    ans_list.val = min_val
                    ans_list.next = ListNode()
                    ans_list = ans_list.next
                    # print("head: ", head)
                    # break
                else:
                    min_prev.next = min_prev.next.next
                    ans_list.val = min_val
                    ans_list.next = ListNode()
                    ans_list = ans_list.next     
            else:
                ans_list.val = min_prev.val
                ans_list.next = None
                return answer
            # count -= 1
            # print("answer: ",answer)
            # print("head: ", head)
        return answer
