# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return
        stack = [(root,[],0)]
        
        while stack:
            node,path,curr_sum = stack.pop()
            curr_sum += node.val
            
            if curr_sum == targetSum and not node.left and not node.right:
                path.append(node.val)
                res.append(path)

            if node.right:
                stack.append((node.right,path+[node.val],curr_sum))
            if node.left:
                stack.append((node.left,path+[node.val],curr_sum))
                
        return res