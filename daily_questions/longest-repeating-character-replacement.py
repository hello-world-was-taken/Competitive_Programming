# https://leetcode.com/problems/longest-repeating-character-replacement/



class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_dic = defaultdict(int)
        max_count = 0
        
        left = 0
        right = 0
        for right in range(len(s)):
            count_dic[s[right]] += 1
            max_count = max(max_count, count_dic[s[right]]) # the maximum frequency untill now
            
            if (right - left + 1) - max_count > k:
                count_dic[s[left]] -= 1
                left += 1
        
        return max_count + min(k, len(s) - max_count)
