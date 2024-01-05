# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def compare(p,q):
            if p.val != q.val:
                return False
            q = deque([(p,q)])
            while q:
                size = len(q)

                for _ in range(size):
                    n1,n2 = q.popleft()
                    if not n1 and n2 or n1 and not n2:
                        return False
                    elif n1 and n2 and n1.val != n2.val:
                        return False
                    if n1 and n2:
                        q.append((n1.left,n2.left))
                        q.append((n1.right,n2.right))
            return True
            
        
        q = deque([root])
        
        while q:
            size = len(q)
            
            for _ in range(size):
                node = q.popleft()
                if compare(node,subRoot):
                    return True
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return False