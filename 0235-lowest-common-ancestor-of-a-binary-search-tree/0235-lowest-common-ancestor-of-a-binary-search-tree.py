# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node,n1,n2):
            if not node:
                return
            if node == n1 or node == n2:
                return node
            ln = dfs(node.left,n1,n2)
            rn = dfs(node.right,n1,n2)
            
            if ln and rn:
                return node
            if ln: return ln
            if rn: return rn
            
        return dfs(root,p,q)
    
    
    