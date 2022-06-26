# https://leetcode.com/problems/longest-palindromic-substring/



class Solution:
    def longestPalindrome(self, s: str) -> str:
        long = 0
        ans_final = [0, 0]
        def pali(left, right):
            ans = [0, 0]
            while left > -1 and right < len(s):
                if s[left] == s[right]:
                    ans = [left, right+1]
                    left -= 1
                    right += 1
                else:
                    break
            return ans
        
        for i in range(len(s)):
            odd = pali(i, i)
            even = pali(i, i + 1)
            
            temp_ans = odd if odd[1] - odd[0] > even[1] - even[0] else even
            ans_final = temp_ans if temp_ans[1] - temp_ans[0] > ans_final[1] - ans_final[0] else ans_final
             
        return s[ans_final[0]: ans_final[1]]
