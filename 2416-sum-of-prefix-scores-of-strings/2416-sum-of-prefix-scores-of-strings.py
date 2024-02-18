class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def add_word(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.prefix_count += 1
    
    def getScore(self,word):
        curr = self.root
        score = 0
        
        for c in word:
            curr = curr.children[c]
            score += curr.prefix_count
            
        return score
            
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
        trie = Trie()
        
        for word in words:
            trie.add_word(word)
            
        res = []
        for word in words:
            res.append(trie.getScore(word))
            
        return res