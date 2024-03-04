# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_sum = [float("-inf")]
        
        def dfs(node):
            if not node:
                return 0
            
            left = max(0,dfs(node.left))
            right = max(0,dfs(node.right))
            max_sum[0] = max(max_sum[0],left + right+node.val)
            
            return node.val + max(left,right)
        
        dfs(root)
        return max_sum[0]