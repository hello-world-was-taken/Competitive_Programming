#https://leetcode.com/problems/online-election/


class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        
        self.max_at_time = [0] * len(times)
        self.dic = {}
        max_person_count = [-1, -1]
        for i in range(len(self.times)): # because best is an index while using binary search
            if self.dic.get(self.persons[i]) == None:
                self.dic[self.persons[i]] = 1
            else:
                self.dic[self.persons[i]] += 1
            if self.dic[self.persons[i]] > max_person_count[1]:
                max_person_count[0] = self.persons[i]
                max_person_count[1] = max(max_person_count[1], self.dic[self.persons[i]])
            if self.dic[self.persons[i]] == max_person_count[1]:
                max_person_count[0] = self.persons[i]
            
            self.max_at_time[i] = max_person_count[0]
            
    def q(self, t: int) -> int:
        left = 0
        right = len(self.times) - 1
        best = None
        
        while left <= right:
            mid = sum([left, right])//2
            if self.times[mid] > t:
                right = mid - 1
            else:
                best = mid
                left = mid + 1
        return self.max_at_time[best]
            
        
        
        
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
