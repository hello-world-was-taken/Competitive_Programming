# https://leetcode.com/problems/detect-squares/


class DetectSquares:

    def __init__(self):
        self.points_count = Counter()        
        self.x_coord = defaultdict(set)
        
    def add(self, point: List[int]) -> None:
        x ,y = point
        self.points_count[x,y] += 1
        self.x_coord[x].add( y ) 
        
    def count(self, point: List[int]) -> int:
        x1 ,y1 = point[0], point[1]
        ans = 0
        
        for y2 in self.x_coord[x1]:
            if y1 == y2: continue
            
            side_length = y2 - y1
            x2a = x1 + side_length
            x2b = x1 - side_length
            
            ans += self.points_count [x1,y2] * self.points_count [x2a, y2 ] * self.points_count [x2a,y1] 
            ans += self.points_count [x1,y2] * self.points_count [x2b, y2 ] * self.points_count [x2b,y1] 
        return ans
