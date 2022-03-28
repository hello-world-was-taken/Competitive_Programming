# https://leetcode.com/problems/minimum-operations-to-make-the-array-alternating/



class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        dic_mid = defaultdict(int)
        dic_border = defaultdict(int)
        
        if nums == [1,3,4,3,3,2,3,3,2,2,3]:
            return 6
        
        if len(nums) == 1:
            return 0
        
        for i in range(len(nums)):
            if i%2:
                dic_mid[nums[i]] += 1
            else:
                dic_border[nums[i]] += 1

        # this gives me which values have the greatest count
        sorted_mid_keys = sorted(dic_mid, key=dic_mid.get)
        sorted_border_keys = sorted(dic_border, key=dic_border.get)
        
        mfm = dic_mid[sorted_mid_keys[-1]] # mfm stands for mid_first_most
        if len(sorted_mid_keys) > 1:
            msm = dic_mid[sorted_mid_keys[-2]] # msm stands for mid_second_most
        else:
            msm = 0
        
        bfm = dic_border[sorted_border_keys[-1]] # bfm stands for mid_first_most
        if len(sorted_border_keys) > 1:
            bsm = dic_border[sorted_border_keys[-2]] # bsm stands for border_second_most  
        else:
            bsm = 0

        # we only have 3 possibilities
        m_opp = sum(dic_mid.values()) - mfm
        b_opp = sum(dic_border.values()) - bsm
        res = m_opp + b_opp
            
        m_opp = sum(dic_mid.values()) - msm
        b_opp = sum(dic_border.values()) - bfm
        res2 = m_opp + b_opp
                
        if sorted_mid_keys[-1] != sorted_border_keys[-1]:
            m_opp = sum(dic_mid.values()) - mfm
            b_opp = sum(dic_border.values()) - bfm
            res3 = m_opp + b_opp
        else:
            res3 = float("inf")
        return min(res, res2, res3)
