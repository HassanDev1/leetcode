# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]
        
        def dfs(node,prev):
            if not node:
                return 
            if prev <= node.val:
                count[0] += 1
                prev = node.val
            dfs(node.left,prev)
            dfs(node.right,prev)
        dfs(root,root.val)
        return count[0]