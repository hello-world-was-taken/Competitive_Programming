# https://leetcode.com/problems/binary-watch/


class Solution:
    def buildNumFromBinary(self, bitmask):
        hour = minute = 0
        for i in range(10):
            if i < 6 and bitmask & (1 << i):
                minute += 1 << i
            elif i >= 6 and bitmask & (1 << i):
                hour += 1 << (i - 6)
                
        time = ""
        if hour < 12 and minute < 60:
            time += f"{hour}:"
            if minute < 10:
                time += f"0{minute}"
            else:
                time += f"{minute}"
        
        return time
        
        
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        final_ans = set()
        def backtrack(bit, bitmask, turned_on):
            if bit > 9:
                if turned_on == 0:
                    time = self.buildNumFromBinary(bitmask)
                    if len(time):
                        final_ans.add(time)
                return
            
            # turn the curr bit
            if turned_on > 0:
                backtrack(bit + 1, bitmask | (1 << bit), turned_on - 1)
            
            backtrack(bit + 1, bitmask, turned_on)
        backtrack(0, 0, turnedOn)
        return final_ans
