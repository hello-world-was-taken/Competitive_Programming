# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/



class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])# sorting it based on the ending value
        
        # do it for the first round since len(points) >= 1
        just_popped = points[0][1]
        arrows_fired = 1
        for i in range(1, len(points)):
            if points[i][0] <= just_popped <= points[i][1]:
                pass
            else:
                just_popped = points[i][1]
                arrows_fired += 1
        return arrows_fired
