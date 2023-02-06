# https://leetcode.com/problems/counting-words-with-a-given-prefix/


class TrieNode:
    def __init__(self):
        self.count = 1
        self.children = {}

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        self.root = TrieNode()
        curr = self.root
        
        for word in words:
            for letter in word:
                if letter in curr.children:
                    curr.children[letter].count += 1
                else:
                    curr.children[letter] = TrieNode()
                curr = curr.children[letter]
            curr = self.root
        
        curr = self.root  
        for i, pre in enumerate(pref):
            if i == len(pref)-1:
                if pre in curr.children:
                    return curr.children[pre].count
                else:
                    return 0
            else:
                if pre in curr.children:
                    curr = curr.children[pre]
                else:
                    return 0
