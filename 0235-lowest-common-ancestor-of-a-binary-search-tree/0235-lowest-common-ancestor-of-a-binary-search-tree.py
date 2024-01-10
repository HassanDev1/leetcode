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
        left_side = self.lowestCommonAncestor(root.left,p,q)
        right_side = self.lowestCommonAncestor(root.right,p,q)
        if left_side and right_side:
            return root
        if left_side:
            return left_side
        if right_side:
            return right_side
        