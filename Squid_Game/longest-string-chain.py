# https://leetcode.com/problems/longest-string-chain/


class Solution:    
    def longestStrChain(self, words: List[str]) -> int:
        graph = defaultdict(list)
        words = set(words)
        dp = defaultdict(lambda: 1)
        sorted_words = sorted(words, key=lambda word: -len(word))
        
        for word in sorted_words:
            for i in range(len(word)):
                new = word[:i] + word[i+1:]
                if new in words:
                    graph[word].append(new)
                    dp[new] = max(dp[new], dp[word] + 1)
        
        if dp.values():
            return max(dp.values())
        return 1
