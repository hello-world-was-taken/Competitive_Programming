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
        curr_x , curr_y = point
        ans = 0
        
        for y in self.x_coord[curr_x]:    
            if curr_y == y:
                continue
            
            side = y -  curr_y
            x1 = curr_x + side
            x2 = curr_x - side
        
            ans += self.points_count [curr_x,y] * self.points_count [x1, y ] * self.points_count [x1, curr_y] 
            ans += self.points_count [curr_x,y] * self.points_count [x2, y ] * self.points_count [x2, curr_y] 
        
        return ans
