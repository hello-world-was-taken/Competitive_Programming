#https://leetcode.com/problems/dota2-senate/



class Solution:
    def find_next_letter(self, letter, senate, index):
        j = index + 1
        while j < len(senate):
            if senate[j] == letter:
                return j
            j += 1
            
        for i,v in enumerate(senate):
            if v == letter:
                return i
        return -1
            
            
    def predictPartyVictory(self, senate: str) -> str:
        self.senate = senate
        senate_count = defaultdict(int)
        senate_as_list = []
        
        for letter in senate:
            senate_as_list.append(letter)

            if letter == 'D':
                senate_count['D'] += 1
            else:
                senate_count['R'] += 1
        
        i = 0
        while True:
            i %= len(senate_as_list)
            if senate_as_list[i] == 'D':
                if senate_count['R'] > 0:
                    senate_count['R'] -= 1
                    next_opp_senate = self.find_next_letter('R', senate_as_list, i)
                    if next_opp_senate != -1:
                        senate_as_list[next_opp_senate] = -1
                else:
                    return "Dire"
                
            elif senate_as_list[i] == 'R':
                if senate_count['D'] > 0:
                    senate_count['D'] -= 1
                    next_opp_senate = self.find_next_letter('D', senate_as_list, i)
                    if next_opp_senate != -1:
                        senate_as_list[next_opp_senate] = -1
                else:
                    return "Radiant"
            i += 1
