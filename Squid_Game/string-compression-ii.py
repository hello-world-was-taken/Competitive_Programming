# https://leetcode.com/problems/string-compression-ii/


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len( s )
        
        @lru_cache(None)
        def dp(idx, prev, prev_count, k_left):
            if idx == n:
                return 0
            
            res = float("inf")
            if prev == s[idx]:
                if prev_count == 1 or prev_count == 9 or prev_count == 99:
                    res = min( res, 1 + dp( idx + 1, prev, prev_count + 1, k_left) )
                else:
                    res = min( res, dp( idx + 1, prev, prev_count + 1, k_left) )
            else:
                if k_left > 0:
                    res = min( res, dp( idx + 1, prev, prev_count, k_left - 1) )
                res = min( res, 1 + dp( idx + 1, s[idx], 1, k_left) )
                
            return res
        
        return dp( 0, "", 0, k)
                
