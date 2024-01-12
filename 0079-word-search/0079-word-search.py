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
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        root = TrieNode()
        root.addWord(word)
        
        ROWS,COLS = len(board),len(board[0])
        
        res,visited = set(),set()
        
        def dfs(r,c,node,res,w):
            if r == ROWS or c == COLS or c<0 or r < 0 or board[r][c] not in node.children or (r,c) in visited:
                return
            visited.add((r,c))
            node = node.children[board[r][c]]
            w += board[r][c]
            if node.isWord:
                res.add(w)
                
            dfs(r+1,c,node,res,w)
            dfs(r-1,c,node,res,w)
            dfs(r,c+1,node,res,w)
            dfs(r,c-1,node,res,w)
         
            visited.remove((r,c))
            
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c, root,res,"")
      
        return len(res) > 0
        