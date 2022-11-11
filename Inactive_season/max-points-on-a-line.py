# https://leetcode.com/problems/max-points-on-a-line/


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 1
        
        def find_slope(x, y, x1, y1):
            if x1 == x: return float("inf")
            return (y1-y)/(x1-x)
        
        dic = defaultdict(lambda: 1)
        
        for i in range(n):
            slope = None
            for j in range(n):
                if i != j:
                    slope = find_slope(points[i][0], points[i][1], points[j][0], points[j][1])
                    dic[(i, slope)] += 1
                    ans = max(dic[(i, slope)], ans)
        return ans
