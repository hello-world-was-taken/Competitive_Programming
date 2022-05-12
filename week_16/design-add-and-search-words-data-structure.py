# https://leetcode.com/problems/design-add-and-search-words-data-structure/



class TrieNode:
    def __init__(self):
        self.isTerminal = False
        self.children = {}

class WordDictionary:

    def __init__(self):
         self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode()
            curr = curr.children[letter]
  
        curr.isTerminal = True

    def search(self, word: str) -> bool:
        return self.helper(word, self.root, 0)
            
    def helper(self, word, node, index):
        if index >= len(word):
            return node.isTerminal
        
        if word[index] != '.' and word[index] not in node.children:
            return False
        
        if word[index] == ".":
            for key in node.children:
                if self.helper(word, node.children[key], index + 1):
                    return True
            return False
        return self.helper(word, node.children[word[index]], index + 1)     
