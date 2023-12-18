# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return []
        
        stack = [(1,root)]
        inorder = []
        
        while stack:
            num,node = stack.pop()
            
            if num == 1:
                num += 1
                stack.append((num,node))
                if node.left:
                    stack.append((1,node.left))
            elif num == 2:
                num += 1
                stack.append((num,node))
                inorder.append(node.val)
                if node.right:
                    stack.append((1,node.right))
                    
                    
        return inorder
                    
                    
                
                    