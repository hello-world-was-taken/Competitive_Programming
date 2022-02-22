#https://leetcode.com/problems/top-k-frequent-elements/


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = []
        
        dic = {}
        
        for i in nums:
            temp = dic.get(i)
            if temp == None:
                dic[i] = 1
            else:
                dic[i] += 1
        print(dic)
        new_nums = []
        for i in list(dic.keys()):
            new_nums.append((-dic[i], i))
        
        heapq.heapify(new_nums)
        print(new_nums)
        
        ans_list = []
        for i in range(k):
            ans_list.append(heapq.heappop(new_nums)[1])
            
        return ans_list
