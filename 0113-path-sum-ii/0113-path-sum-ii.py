# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        def dfs(node,curr_sum,path):
            if not node:
                return 
            curr_sum += node.val
           
            
            if curr_sum == targetSum and not node.left and not node.right:
                path.append(node.val)
                res.append(path)
                
            dfs(node.left,curr_sum,path+[node.val])
            dfs(node.right,curr_sum,path+[node.val])
            
            
        dfs(root,0,[])
        return res