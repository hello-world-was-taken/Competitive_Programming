#https://leetcode.com/problems/kth-largest-element-in-a-stream/


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapq.heapify(self.nums)
        self.k = k
        print(self.nums)
        while self.k < len(self.nums):
            heapq.heappop(self.nums)
        print(self.nums)


    def add(self, val: int) -> int:
        if len(self.nums) == self.k and val <= self.nums[0]:
            return self.nums[0]
            print(self.nums)
        elif len(self.nums) == self.k:
            heapq.heappop(self.nums)
            heapq.heappush(self.nums, val)
            return self.nums[0]
        elif len(self.nums) < self.k:
            heapq.heappush(self.nums, val)
            
        if len(self.nums) == self.k:
            return self.nums[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
