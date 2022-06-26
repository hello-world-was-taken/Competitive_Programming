# https://leetcode.com/problems/longest-common-prefix/



class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.count = 0
        self.children = {}
        
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.root = TrieNode("")
        longest = float("inf")
        
        # build trie
        for j, word in enumerate(strs):
            curr = self.root
            if word == "":
                return ""
            for i, letter in enumerate(word):
                if letter not in curr.children:
                    curr.children[letter] = TrieNode(letter)
                curr.children[letter].count += 1
                curr = curr.children[letter]
              
        curr = self.root
        ans = ""
        while len(curr.children):
            if len(list(curr.children.keys())):
                if curr.children[list(curr.children.keys())[0]].count == len(strs):
                    ans += curr.children[list(curr.children.keys())[0]].letter
                else:
                    break
                curr = curr.children[list(curr.children.keys())[0]]

        return ans    
