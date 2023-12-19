# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def check(node):
            if not node:
                return 0
            ls = check(node.left)
            if ls == -1: return -1
            
            rs = check(node.right)
            if rs == -1:
                return -1
            
            if abs(ls-rs) > 1:return -1
            return 1 + max(ls,rs)
        
        return check(root) != -1
        