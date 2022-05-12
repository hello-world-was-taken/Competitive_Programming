# https://leetcode.com/problems/isomorphic-strings/



class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        st_map = {}
        ts_map = {}
        
        i = 0
        while i < len(s):
            if s[i] not in st_map:
                st_map[s[i]] = t[i] # map s[i] -> t[i]
            else:
                if st_map[s[i]] != t[i]:
                    return False

            if t[i] not in ts_map:
                ts_map[t[i]] = s[i]
                # print(ts_map[t[i]], " -> ", s[i])
            else:
                if ts_map[t[i]] != s[i]:
                    return False
                
            i += 1
        return True
