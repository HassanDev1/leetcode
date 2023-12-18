# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        
        if not root:
            return []
        
        res = []
        
        stck1 = [root]
        stck2 = []
        
        while stck1:
            node = stck1.pop()
            stck2.append(node)
            
            if node.left:
                stck1.append(node.left)
            if node.right:
                stck1.append(node.right)
                
        while stck2:
            node = stck2.pop()
            res.append(node.val)
            
        return res
        