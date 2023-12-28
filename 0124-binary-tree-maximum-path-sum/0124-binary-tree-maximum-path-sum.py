# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_gain = [float("-inf")]
        def getmax(node):
            if not node:
                return 0
            
            left_gain = max(getmax(node.left),0)
            right_gain = max(getmax(node.right),0)
            curr_path = node.val + left_gain+right_gain
            max_gain[0] = max(max_gain[0],curr_path)
            
            return node.val + max(left_gain,right_gain)
        getmax(root)                           
        return max_gain[0]
        