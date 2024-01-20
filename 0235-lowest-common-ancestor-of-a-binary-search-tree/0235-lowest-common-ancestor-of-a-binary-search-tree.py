# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def get_lca(node,p,q):
            if not node:
                return
            if node == p or node ==q:
                return node
            ls = get_lca(node.left,p,q)
            rs = get_lca(node.right,p,q)
            if ls and rs:
                return node
            if ls:
                return ls
            if rs:
                return rs
        return get_lca(root,p,q)
        