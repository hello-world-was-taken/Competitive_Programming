#https://leetcode.com/problems/design-linked-list/

class MyLinkedList:

    def __init__(self):
        self.head = self
        self.val = None
        self.next = None
        

    def get(self, index: int) -> int:
        temp = self.head
        count = 0
        if self.head != None and self.head.val == None:
            return -1
        if index == 0 and self.head != None:
            return self.head.val
        while count < index and temp != None:
            temp = temp.next
            count += 1
        if temp == None:
            return -1
        else:
            return temp.val

    def addAtHead(self, val: int) -> None:
        if self.val != None:
            addedValue = MyLinkedList()
            addedValue.val = val
            addedValue.next = self.head
            self.head = addedValue
        elif self.val == None:
            self.val = val

    def addAtTail(self, val: int) -> None:
        if self.val == None:
            self.val = val
            return
        addedValue = MyLinkedList()
        addedValue.val = val
        tempTail = self.head
        tempHead = self.head
        while tempHead != None:
            tempTail = tempHead # keeping track of the previous
            tempHead = tempHead.next
        tempTail.next = addedValue

    def addAtIndex(self, index: int, val: int) -> None:
        addedValue = MyLinkedList()
        addedValue.val = val
        count = 0
        tempHead = self.head
        if index == 0:
            self.addAtHead(val)
            return
        while tempHead != None and count < index - 1:
            tempHead = tempHead.next
            count += 1
        if tempHead != None:   
            tempHeadNext = tempHead.next
            tempHead.next = addedValue
            addedValue.next = tempHeadNext

    def deleteAtIndex(self, index: int) -> None:
        count = 0
        tempHead = self.head
        prev = tempHead
        if index == 0:
            self.head = self.head.next
            return
        while count < (index) and tempHead != None:
            prev = tempHead
            tempHead = tempHead.next
            count += 1
        if tempHead != None and tempHead.next == None:
            prev.next = None
        elif tempHead != None:
            prev.next = tempHead.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
