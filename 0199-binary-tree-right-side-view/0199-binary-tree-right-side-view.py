# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root:
            return
        
        q = deque([root])
        res = []
        
        while q:
            size = len(q)
            
            tmp = None
            
            for _ in range(size):
                node = q.popleft()
                tmp = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(tmp)
            
        return res
        