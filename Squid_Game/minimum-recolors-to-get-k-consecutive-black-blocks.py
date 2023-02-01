# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = 0
        left = right = 0
        n = len(blocks)
        ans = float('inf')
        
        while right < n:
            if blocks[right] == 'W':
                white_count += 1

            if right - left + 1 == k:
                ans = min(ans, white_count)
                
                if blocks[left] == 'W':
                    white_count -= 1
                left += 1
                
            right += 1
            
        return ans
                
