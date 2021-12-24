#QUESTION
#https://leetcode.com/problems/design-circular-deque/



class MyCircularDeque:

    def __init__(self, k: int):
        self.my_circular_deque = [None] * k
        self.limit = k
        self.front = 0
        self.rear = 0
        self.occupied = 0
    def insertFront(self, value: int) -> bool:
        if self.isFull(): return False
        self.front = (self.front + self.limit - 1) % self.limit
        self.my_circular_deque[self.front] = value
        self.occupied += 1
        return True
    def insertLast(self, value: int) -> bool:
        if self.isFull(): return False
        self.my_circular_deque[self.rear] = value
        self.rear = (self.rear + 1) % self.limit
        self.occupied += 1
        return True
    def deleteFront(self) -> bool:
        if self.isEmpty(): return False
        self.front = (self.front + 1) % self.limit
        self.occupied -= 1
        return True
    def deleteLast(self) -> bool:
        if self.isEmpty(): return False
        self.rear = (self.rear - 1) % self.limit
        self.occupied -= 1
        return True
    def getFront(self) -> int:
        if self.isEmpty(): return -1
        return self.my_circular_deque[self.front]
    def getRear(self) -> int:
        if self.isEmpty(): return -1
        return self.my_circular_deque[self.rear-1]
    def isEmpty(self) -> bool:
        return True if self.occupied == 0 else False

    def isFull(self) -> bool:
        return True if self.occupied == self.limit else False
