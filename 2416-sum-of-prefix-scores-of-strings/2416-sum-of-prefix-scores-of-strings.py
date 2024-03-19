
class TrieNode:
    def __init__(self):
        self.children = {}
        self.score = 0
        
class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()
        
        
    def insert_word(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
            curr.score += 1
            
    def return_score(self,word):
        count = 0
        curr = self.root
        for c in word:
            curr = curr.children[c]
            count += curr.score
        return count
    

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = PrefixTrie()
        
        for word in words:
            trie.insert_word(word)
      
        res = []
        for word in words:
            res.append(trie.return_score(word))
            
        return res