# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def get_height(node):
            if not node:
                return 0
            left_h = get_height(node.left)
            right_h = get_height(node.right)
            return 1 + max(left_h,right_h)
        
        diam = 0
        stack = [root]
        
        while stack:
            node = stack.pop()
            
            lh = get_height(node.left)
            rh = get_height(node.right)
            curr = lh + rh
            diam = max(diam,curr)
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return diam
        
        