# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left),get_height(node.right))
        if not root:
            return 0
        q = deque([root])
        diam = 0
        while q:
            node = q.popleft()
            lh = get_height(node.left)
            rh = get_height(node.right)
            curr_height = lh + rh
            
            diam = max(diam,curr_height)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
        return diam
            
        