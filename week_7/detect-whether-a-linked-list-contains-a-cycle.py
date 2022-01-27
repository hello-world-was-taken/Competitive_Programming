#https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem

# There is also a two pointer implementation
def has_cycle(head):
    my_set = set()
    while head != None:
        if head in my_set:
            return 1
        my_set.add(head)
        head = head.next
    return 0
