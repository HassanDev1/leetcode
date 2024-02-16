class TrieNode:
    def __init__(self):
        self.children = {}
        self.pref_count = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.pref_count += 1
            
    def searchWord(self,word):
        curr = self.root
        score = 0
        for c in word:
            curr = curr.children[c]
            score += curr.pref_count
        return score
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        res = []
        
        prefix = Trie()
        
        for word in words:
            prefix.addWord(word)
            
        for word in words:
            count = prefix.searchWord(word)
            res.append(count)
            
        return res
            