# https://leetcode.com/problems/longest-substring-without-repeating-characters/



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = 0
        visited = defaultdict(lambda: (-1))
        ans = 0
        
        while right < len(s):
            if visited[s[right]] != -1:
                left = max(visited[s[right]] + 1, left)
                visited[s[right]] = -1
            else:
                visited[s[right]] = right
                ans = max(ans, right - left + 1)
                right += 1
                
        return ans
                
