# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root:
            return
        if root.val == p.val or root.val == q.val:
            return root
        left_node = self.lowestCommonAncestor(root.left,p,q)
        right_node = self.lowestCommonAncestor(root.right,p,q)
        if left_node and right_node:
            return root
        if left_node:
            return left_node
        if right_node:
            return right_node
        