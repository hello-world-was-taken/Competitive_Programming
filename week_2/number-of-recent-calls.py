#QUESTION
#https://leetcode.com/problems/number-of-recent-calls/

class RecentCounter:

    def __init__(self):
        self.stack = []
        self.min = 0

    def ping(self, t: int) -> int:
        self.stack.append(t)
        arr_len = len(self.stack)
        range_ = t-3000
        if range_ <= 0:
            return arr_len
        
        for i in range(self.min, len(self.stack)):
            if self.stack[i] >= range_:
                self.min = i
                return arr_len - i


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
