#QUESTION
#https://leetcode.com/problems/k-closest-points-to-origin/submissions/

# using a built in python sorting algorithm using the following comparator
def greater_distance(point_distance):
    return point_distance[0]

class Solution:
    def distance(self, point_x, point_y):
        return sqrt(point_x**2 + point_y**2)
    
    def kClosest(self, points, k):
        point_distance = []
        for point in points:
            point_distance.append((self.distance(point[0],point[1]),point))
        
        point_distance.sort(key=greater_distance)
        result=[]
        
        for i in range(k):
            result.append(point_distance[i][1])
        return result
