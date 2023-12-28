# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node,s,d):
            if not node:
                return
            if node.val == s.val:
                return node
            if node.val == d.val:
                return node
            left = dfs(node.left,s,d)
            right = dfs(node.right,s,d)
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
        return dfs(root,p,q)
        