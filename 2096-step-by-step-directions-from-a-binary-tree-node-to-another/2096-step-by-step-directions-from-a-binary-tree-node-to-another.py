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
            left_side = get_lca(node.left,p,q)
            right_side = get_lca(node.right,p,q)
            if left_side and right_side:
                return node
            if left_side:
                return left_side
            if right_side:
                return right_side
        root = get_lca(root,startValue,destValue)
        
        stack = [(root,"")]
        sp = dp = ""
        while stack:
            node,path = stack.pop()
            
            if node.val == startValue:
                sp = path
            if node.val == destValue:
                dp = path
                
            if node.left:
                stack.append((node.left,path+"L"))
            if node.right:
                stack.append((node.right,path+"R"))
                
        return "U"*len(sp)+dp
        
        