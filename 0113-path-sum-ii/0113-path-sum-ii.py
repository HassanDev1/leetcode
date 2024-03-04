# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        res = []
        def dfs(node,curr_sum,temp):
            if not node:
                return 0
            curr_sum += node.val
            temp.append(node.val)
            if curr_sum == targetSum and not node.left and not node.right:
                res.append(temp.copy())
                
            dfs(node.left,curr_sum,temp)
            dfs(node.right,curr_sum,temp)
            temp.pop()
            
        dfs(root,0,[])
        return res