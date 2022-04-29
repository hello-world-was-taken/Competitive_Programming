# https://leetcode.com/problems/implement-trie-prefix-tree/



class TrieNode:
    def __init__(self, letter):
        self.letter = letter
        self.isTerminal = False
        self.children = {}

class Trie:

    def __init__(self):
        self.root = TrieNode("")

    def insert(self, word: str) -> None:
        curr = self.root
        
        for letter in word:
            if letter not in curr.children:
                curr.children[letter] = TrieNode(letter)
            curr = curr.children[letter]
            
        curr.isTerminal = True

    def search(self, word: str) -> bool:
        curr = self.root
        
        for letter in word:
            if letter not in curr.children:
                return False
            else:
                curr = curr.children[letter]
                
        return curr.isTerminal
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        
        for letter in prefix:
            if letter not in curr.children:
                return False
            else:
                curr = curr.children[letter]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
