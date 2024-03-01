class TrieNode:
    def __init__(self):
        self.children = {}
        self.prefix_count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self,word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
            curr.prefix_count += 1
            
            
    def return_score(self,word):
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
            trie.addWord(word)
            
        res = []
        
        for word in words:
            res.append(trie.return_score(word))
            
        return res
            
        
            