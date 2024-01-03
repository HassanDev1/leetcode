# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_path = [float("-inf")]
        
        def get_max(node):
            if not node:
                return 0
            left_gain = max(get_max(node.left),0)
            right_gain = max(get_max(node.right),0)
            path = node.val + left_gain + right_gain
            max_path[0] = max(max_path[0],path)
            return node.val + max(left_gain,right_gain)
        get_max(root)
        return max_path[0]
        