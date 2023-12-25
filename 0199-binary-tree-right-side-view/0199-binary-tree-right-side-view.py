# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q = deque([root])
        if not root:
            return []
        res = []
        while q:
            size = len(q)
            tmp = None
            for _ in range(size):
                node = q.popleft()
                temp = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            res.append(temp)
        return res
        