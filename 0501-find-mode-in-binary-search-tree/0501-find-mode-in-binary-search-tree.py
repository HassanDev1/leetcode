# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = {}
        
        res = []
        
        def dfs(node):
            if not node:
                return
            freq[node.val] = freq.get(node.val,0)+1
           
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        max_freq = max(freq.values())
        
        for key in freq:
            if freq[key] == max_freq:
                res.append(key)
            
       
        return res
        
        