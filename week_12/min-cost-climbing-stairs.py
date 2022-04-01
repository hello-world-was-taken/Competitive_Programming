# https://leetcode.com/problems/min-cost-climbing-stairs/



class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        behind_two_step = cost[0]
        behind_one_step = cost[1]
        
        for i in range(2,len(cost)):
            cost[i] += min(behind_two_step, behind_one_step)
            behind_two_step = behind_one_step
            behind_one_step = cost[i]
        return min(cost[-1], cost[-2])
                
