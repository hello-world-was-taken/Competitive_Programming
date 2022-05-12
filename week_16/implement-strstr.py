# https://leetcode.com/problems/implement-strstr/



class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = j = 0
        nearest = i
        
        if len(haystack) < len(needle):
            return -1
        
        while i < len(haystack) and j < len(needle):
            
            if haystack[i] == needle[j]:
                k = i
                first = False
                while k < len(haystack) and j < len(needle):
                    if haystack[k] == needle[0]:
                        if k > i and not first:
                            nearest = k
                            first = True
                    if haystack[k] == needle[j]:
                        k += 1
                        j += 1
                    else:
                        break
                    
                    if j == len(needle):
                        return i
            j = 0
            i = max(nearest, i + 1)
                               
        return -1
