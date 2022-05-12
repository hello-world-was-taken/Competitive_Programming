# https://leetcode.com/problems/prefix-and-suffix-search/



class TrieNode:
    def __init__(self):
        self.words_index = []
        self.suffix = set()
        self.children = {}

class WordFilter:

    def __init__(self, words: List[str]):
        self.root_pre = TrieNode()
        self.root_suf = TrieNode()
        
        for i, word in enumerate(words):
            # for pre
            curr = self.root_pre
            for letter in word:
                if letter not in curr.children:
                    curr.children[letter] = TrieNode()
                    
                curr.children[letter].words_index.append(i)
                # print("letter: ", letter, "word with letter: ", i)
                curr = curr.children[letter]
            curr = self.root_pre
            
            # for suffix reversed
            curr = self.root_suf
            for letter in reversed(word):
                if letter not in curr.children:
                    curr.children[letter] = TrieNode()
                    
                curr.children[letter].suffix.add(i)
                curr = curr.children[letter]
            curr = self.root_suf

    def f(self, prefix: str, suffix: str) -> int:
        curr = self.root_pre
        for letter in prefix:
            if letter not in curr.children:
                return -1
            else:
                curr = curr.children[letter]
        
        list_of_index_for_words_with_prefix = curr.words_index

        curr = self.root_suf
        ans = -1
        for letter in reversed(suffix):
            if letter not in curr.children:
                return -1
            else:
                curr = curr.children[letter]

        list_of_index_for_words_with_suffix = curr.suffix
        for i in reversed(list_of_index_for_words_with_prefix):
            if i in list_of_index_for_words_with_suffix:
                return i
        return -1
