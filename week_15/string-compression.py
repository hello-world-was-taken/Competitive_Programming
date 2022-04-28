# https://leetcode.com/problems/string-compression/



class Solution:
    def compress(self, chars: List[str]) -> int:
        # I know it says constant space. But hey, what the hell, right?
        s = chars
        count = 1
        ans = []
        i = 0
        while i < (len(s) -1):
            if s[i] != s[i+1]:
                ans.append(s[i])
                if count == 1:
                    pass
                elif count < 10:
                    ans.append(str(count))
                else:
                    t = str(count)
                    for j in t:
                        ans.append(str(j))
                count = 0
            i += 1
            count += 1
        
        if len(chars) > 1:
            ans.append(s[i])
            if count == 1:
                pass
            elif count < 10:
                    ans.append(str(count))
            else:
                t = str(count)
                for k in t:
                    ans.append(str(k))

        else:
            ans.append(s[i])
        
        for i,v in enumerate(ans):
            chars[i] = v
        return len(ans)
