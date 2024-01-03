# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and  q or p and not q:
            return False
        q = deque([(p,q)])
        
        while q:
            size = len(q)
            
            for _ in range(size):
                n1,n2 = q.popleft()
                if not n1 and n2 or n1 and not n2:
                    return False
                if n1 and n2 and n1.val != n2.val:
                    return False
                if n1 and n2:
                    q.append((n1.left,n2.left))
                
                    q.append((n1.right,n2.right))
        return True