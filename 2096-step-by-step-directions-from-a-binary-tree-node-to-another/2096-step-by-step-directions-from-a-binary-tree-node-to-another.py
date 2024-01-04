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
            ln = get_lca(node.left,p,q)
            rn = get_lca(node.right,p,q)
            
            if ln and rn:
                return node
            if ln:
                return ln
            if rn:
                return rn
        node = get_lca(root,startValue,destValue)
        stack = [(node,"")]
        sp = dp = ""
        while stack:
            root,path = stack.pop()
            
            if root.val == startValue:
                sp = path
            if root.val == destValue:
                dp = path
            if root.left:
                stack.append((root.left,path+"L"))
            if root.right:
                stack.append((root.right,path+"R"))
                
        return "U"*len(sp)+dp
            
            