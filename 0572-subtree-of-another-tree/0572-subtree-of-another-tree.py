# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        q = deque([root])
        def compare(main,sub):
            if not main and not sub:
                return True
            if not main or not sub or main.val != sub.val:
                return False
            return compare(main.left,sub.left) and compare(main.right,sub.right)
        
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
        