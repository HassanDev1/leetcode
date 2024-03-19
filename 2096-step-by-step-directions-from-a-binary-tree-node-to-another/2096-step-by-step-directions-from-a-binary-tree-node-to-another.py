# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def get_lca(node,p,q):
            if not node:
                return
            if node.val == p or node.val == q:
                return node
            l = get_lca(node.left,p,q)
            r = get_lca(node.right,p,q)
            if l and r:
                return node
            if l:
                return l
            if r:
                return r
            
        root = get_lca(root,startValue,destValue)
        sp = dp = ""
        stack = [("",root)]
        
        while stack:
            path,node = stack.pop()
            
            if node.val == startValue:
                sp = path
            if node.val ==destValue:
                dp = path
            if node.left:
                stack.append((path+"L",node.left))
            if node.right:
                stack.append((path+"R",node.right))
                
        return len(sp)*"U" + dp
            
            