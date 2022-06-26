# https://leetcode.com/problems/longest-word-in-dictionary/



class TrieNode():
    def __init__(self):
        self.children = {}
        self.isTerminal = False
        
class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        words.sort()
        final_ans = ""
        
        # build our trie
        for word in words:
            curr = root
            not_terminal = False
            
            for idx, letter in enumerate(word):
                if letter not in curr.children:
                    curr.children[letter] = TrieNode()
                if not curr.children[letter].isTerminal:
                    not_terminal = True
                curr = curr.children[letter]
                
                if idx == len(word) -2 and not not_terminal:
                    final_ans = word if len(word) > len(final_ans) else final_ans
                
                if idx == len(word) -1:  # for the final node, we set isTerminal to True
                    curr.isTerminal = True
                    if len(word) == 1: # if the length is on, it will be an edge case. 
                        final_ans = word if len(word) > len(final_ans) else final_ans
        return final_ans 
