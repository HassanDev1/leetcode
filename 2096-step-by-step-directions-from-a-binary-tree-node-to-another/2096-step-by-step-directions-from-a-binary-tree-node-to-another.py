# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        
        def lca(node,p,q):
            if not node:
                return
            if node.val == p or node.val == q:
                return node
            ln = lca(node.left,p,q)
            rn = lca(node.right,p,q)
            if ln and rn:
                return node
            if ln: return ln
            if rn: return rn
            
        root = lca(root,startValue,destValue)
        sp=dp =""
        
        q = deque([(root,"")])
        
        while q:
            size = len(q)
            
            for _ in range(size):
                node,path = q.popleft()
                
                if node.val == startValue:
                    sp = path
                if node.val == destValue:
                    dp = path
                if node.left:
                    q.append((node.left,path+"L"))
                if node.right:
                    q.append((node.right,path+"R"))
                    
        return "U"*len(sp)+dp