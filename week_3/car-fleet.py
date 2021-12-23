#QUESTION
#https://leetcode.com/problems/car-fleet/


class Solution:
    def distance(self, pos_speed, target):
        return (target - pos_speed[0]) / pos_speed[1]
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr_len = len(position)
        tuple_list = [0] * arr_len
        for i in range(len(position)):
            tuple_list[i] = [position[i], speed[i]]
        tuple_list.sort()
        ans = []
        for i in range(arr_len):
            time_for_each = self.distance(tuple_list[i], target)
            if len(ans) == 0:
                ans.append(time_for_each)
                continue
            while(len(ans) > 0 and time_for_each >= ans[-1]):
                ans.pop()
            ans.append(time_for_each)
            
        return len(ans)
