# https://leetcode.com/problems/earliest-possible-day-of-full-bloom/


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        grow_plant_time = [ (grow, plant) for grow, plant in zip( growTime, plantTime ) ]
        grow_plant_time.sort(reverse=True)
        bloomTime = []
        
        global_plant_time = i = 0
        n = len(plantTime)
        
        while i < n:
            grow_time, plant_time = grow_plant_time[i]
            global_plant_time += plant_time
            bloomTime.append( global_plant_time + grow_time)
            i += 1
            
        return max(bloomTime)
            
        
