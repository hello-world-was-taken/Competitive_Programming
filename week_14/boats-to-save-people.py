# https://leetcode.com/problems/boats-to-save-people/



class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        i = 0
        j = len(people) - 1
        boat_count = 0
        
        # consider the case when there is only one person
        if len(people) == 1:
            return 1
        while i <= j:
            if people[i] + people[j] <= limit:
                boat_count += 1
                i += 1
                j -= 1
            else:
                boat_count += 1
                j -= 1
                
        return boat_count
        
