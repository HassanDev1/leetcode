# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def is_same(p,q):
            if not p and not q:
                return True
            if (p and not q) or (q and not p):
                return False
            if p and q and p.val != q.val:
                return False
            return is_same(p.left,q.left) and is_same(p.right,q.right)
        
        q = deque([root])
        
        while q:
            size = len(q)
            
            for _ in range(size):
                node = q.popleft()
                
                if is_same(node,subRoot):
                    return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return False
        