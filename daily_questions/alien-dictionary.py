# https://practice.geeksforgeeks.org/problems/alien-dictionary/1

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        before, after = defaultdict(set), defaultdict(set)
        letters = set()
        for char in words[0]:
            letters.add(char) 
        for i in range(len(words)-1):
            for char in words[i+1]:
                letters.add(char)
            left, right = 0, 0
            while left < len(words[i]) and right < len(words[i+1]) and words[i][left] == words[i+1][right]:
                left += 1
                right += 1
            if right == len(words[i+1]) and left < len(words[i]):
                return ""
            if left < len(words[i]) and right < len(words[i+1]):
                before[words[i+1][right]].add(words[i][left])
                after[words[i][left]].add(words[i+1][right])

        queue = deque()
        for char in letters:
            if not before[char]:
                queue.append(char)

        res = list()       
        visited = set()
        while queue:
            char = queue.popleft()
            if char in visited:
                continue
            visited.add(char)
            res.append(char)
            for nxt in after[char]:
                before[nxt].remove(char)
                if not before[nxt]:
                    queue.append(nxt)
        
        if len(res) != len(letters):
            return ""
        return "".join(res)
