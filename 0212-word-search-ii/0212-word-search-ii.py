class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
        
    def addWord(self,word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isWord = True
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        
        for w in words:
            root.addWord(w)
            
        res,visit = set(),set()
        COL,ROW = len(board[0]),len(board)
        
        def dfs(r,c,node,res,word):
            if r >= ROW or c >= COL or r < 0 or c < 0 or (r,c) in visit or board[r][c] not in node.children:
                return
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r+1,c,node,res,word) 
            dfs(r-1,c,node,res,word)
            dfs(r,c+1,node,res,word)
            dfs(r,c-1,node,res,word)
            
            visit.remove((r,c))
        
        for r in range(ROW):
            for c in range (COL):
                dfs(r,c,root,res,"")
                
        return list(res)