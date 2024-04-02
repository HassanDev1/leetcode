# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])

        while q:
            size = len(q)

            level = []
            for  _ in range(size):
                node = q.popleft()
                if node:
                    level.append(node.val)
                
                    q.append(node.left)
                
                    q.append(node.right)

            res.append(level)
        return res[:-1]
        