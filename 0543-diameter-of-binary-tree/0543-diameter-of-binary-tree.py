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
            return 1 + max(get_height(node.left),get_height(node.right))
        
        stack =  [root]
        diameter = 0
        while stack:
            node = stack.pop()
            
            lh = get_height(node.left)
            rh = get_height(node.right)
            curr = lh + rh
            diameter = max(diameter,curr)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
                
        return diameter