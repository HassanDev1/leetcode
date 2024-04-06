# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        
        curr_node = root
        parent_node = None
        
        while curr_node:
            if val > curr_node.val:
                parent_node = curr_node
                curr_node = curr_node.right
            else:
                parent_node = curr_node
                curr_node = curr_node.left
                
        new_node = TreeNode(val)
        if not parent_node:
            return new_node
        if parent_node.val < val:
            parent_node.right = new_node
        else:
            parent_node.left = new_node
            
        return root
            