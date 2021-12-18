#QUESTION
#https://leetcode.com/problems/implement-queue-using-stacks/
#Using two stacks we can also move the data backwards and forwards to get the queue like feel, but it is inefficient. 

class MyQueue:

    def __init__(self):
        self.stack_1 = []
        # self.stack_2 = []

    def push(self, x: int) -> None:
        self.stack_1.append(x)

    def pop(self) -> int:
        return self.stack_1.pop(0)

    def peek(self) -> int:
        return self.stack_1[0]

    def empty(self) -> bool:
        return len(self.stack_1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
