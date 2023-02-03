# https://leetcode.com/problems/simplify-path/


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        canonical_path = []
        
        for signal in path:
            if signal == "" or signal == ".":
                continue
            elif signal == "..":
                if canonical_path:
                    canonical_path.pop()
            else:
                canonical_path.append(signal)
                
        return '/' + '/'.join(canonical_path)
