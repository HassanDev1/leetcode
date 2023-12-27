# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        heap = []
        seen = {}
        
        def dfs(node):
            if not node:
                return
            if node.val not in seen:
                seen[node.val] = 1
                heappush(heap,node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        
        for _ in range(1):
            heappop(heap)
            
        return heap[0] if heap else -1