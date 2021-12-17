class MinStack:

    def __init__(self):
        self.min_stack = []
        

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0:
            self.min_stack.append([val, val])
        else:
            if val < self.min_stack[-1][-1]:
                self.min_stack.append([val, val])
            else:
                self.min_stack.append([val, self.min_stack[-1][-1]])
        
        

    def pop(self) -> None:
        temp = self.min_stack.pop()
        return temp[-1]

    def top(self) -> int:
        return self.min_stack[-1][0]

    def getMin(self) -> int:
        return self.min_stack[-1][-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
