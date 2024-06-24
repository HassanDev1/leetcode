# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isIdentical(p,q):
            if not p and not q:
                return True
            if p and not q or not p and q:
                return False
            if p and q and p.val != q.val:
                return False
            return isIdentical(p.left,q.left) and isIdentical(p.right,q.right)
        q = deque([root])
        
        while q:
            size = len(q)
            
            for _ in range(size):
                node = q.popleft()
                if node:
                    if isIdentical(node,subRoot):
                        return True
                    q.append(node.left)
                    q.append(node.right)
                    
                
        