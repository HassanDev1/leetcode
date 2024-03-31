# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node:
                return 0
            left_side = dfs(node.left)
            right_side = dfs(node.right)
            
            if left_side == -1 or right_side == -1:
                return -1
            if abs(left_side - right_side) > 1:
                return -1
            return 1 + max(left_side,right_side)
        return dfs(root) != -1