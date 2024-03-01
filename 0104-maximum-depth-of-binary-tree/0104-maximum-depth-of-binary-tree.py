# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
      
        def get_path(node):
            if not node:
                return 0
            
            left_path = get_path(node.left)
            right_path = get_path(node.right)
            curr = left_path+right_path
            
           
            return 1 + max(left_path,right_path)
        return get_path(root)
       