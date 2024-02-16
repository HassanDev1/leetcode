class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True
        

    def search(self, word: str) -> bool:
        def dfs(root,j):
            curr = root
            for i in range(j,len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(child,i+1):
                            return True
                    return False


                if c not in curr.children:
                    return False
                curr = curr.children[c]
            return curr.is_word
        return dfs(self.root,0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)