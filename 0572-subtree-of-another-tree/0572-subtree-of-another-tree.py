# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(node1,node2):
            if not node1 and not node2:
                return True
            if node1 and not node2 or node2 and not node1:
                return False
            if node1 and node2 and node1.val != node2.val:
                return False
            return is_same(node1.left,node2.left) and is_same(node1.right,node2.right)
        
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