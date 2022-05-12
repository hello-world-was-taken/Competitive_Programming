# https://leetcode.com/problems/top-k-frequent-words/
# I don't see the use of using a trie


class Solution:
    def topKFrequent(self, nums: List[str], k: int) -> List[str]:
        
        dic = Counter(nums)

        new_nums = [(-dic[i], i) for i in list(dic.keys())]
        
        heapq.heapify(new_nums)
            
        return [heapq.heappop(new_nums)[1] for i in range(k)]
