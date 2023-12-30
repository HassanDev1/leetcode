# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def getlca(node,p,q):
            if not node:
                return node
            if node.val == p or node.val == q:
                return node
            left = getlca(node.left,p,q)
            right = getlca(node.right,p,q)
            if left and right:
                return node
            if left:
                return left
            if right:
                return right
        root = getlca(root,startValue,destValue)
        stack = [(root,"")]
        sp = dp = ""
        while stack:
            node,path = stack.pop()
            if node.val == startValue:
                sp = path
            if node.val == destValue:
                dp = path
            if node.left:
                stack.append((node.left,path +"L"))
            if node.right:
                stack.append((node.right,path+"R"))
                
        return "U"*len(sp)+dp
            
        