# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return
        
        root_val = preorder[0]
        mid = inorder.index(root_val)
        
        root = TreeNode(root_val)
        root.left = self.buildTree(preorder[1:mid+1],inorder[:mid+1])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root
        
        