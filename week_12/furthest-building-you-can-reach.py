#https://leetcode.com/problems/furthest-building-you-can-reach/



class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        height_diff = []
        
        for i in range(len(heights)-1):
            if heights[i+1] - heights[i] > 0:
                heappush(height_diff, heights[i+1]-heights[i])
            
            # lets assume we will only use the ladders to and once we finish our ladders, we shall use
            # our bricks to move the smallers of the values which we have previously decided to use 
            # ladders for. STILL IN THE FOR LOOP!

            if len(height_diff) > ladders:
                bricks -= heappop(height_diff)
            
            # print("i: ", i, "diff: ", heights[i+1] - heights[i])
            if bricks < 0:
                # since the 'i' value is always less than the actual buildings given by 1
                # we can simply return the ith value that has negated our bricks.
                return i
        return i +1
            
            # This question is the same as the "how to get to a certain number if we only had two
            # operations like adding 2 and 1" and we first add 2 as much as we can and when it is
            # greater than our target number we do other operations.
