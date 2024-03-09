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
        if not left_side:
            return right_side
        elif not right_side:
            return left_side
        else:
            return root