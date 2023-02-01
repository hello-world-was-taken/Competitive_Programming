# https://leetcode.com/problems/best-team-with-no-conflicts/

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(scores)
        ages_scores = list( zip( ages, scores ) )
        ages_scores.sort()
        res = -1
        
        # top-down gives TLE. Why? I do not know.
        dp = [ score for age, score in ages_scores ]
        for i in range(n):
            curr_age, curr_score = ages_scores[ i ]
            
            for j in range(i-1, -1, -1):
                if curr_score >= ages_scores[j][1]:
                    dp[i] = max( dp[i], curr_score + dp[j] )
            res = max( res, dp[i] )
            
        return res
