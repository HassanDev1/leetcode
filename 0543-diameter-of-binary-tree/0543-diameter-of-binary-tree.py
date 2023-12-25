# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = [0]
        def findHeight(node):
            if not node:
                return 0
            lh = findHeight(node.left)
            rh = findHeight(node.right)
            res[0] = max(res[0],lh+rh)
            return 1 + max(lh,rh)
        findHeight(root)
        return res[0]
            
        