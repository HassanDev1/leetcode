# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        dq = deque([root])
        level = 0
        
        while dq:
            
            size = len(dq)
            if level %2 != 0:
                l,r = 0,size-1
                while l < r:
                    dq[l].val,dq[r].val = dq[r].val,dq[l].val
                    l += 1
                    r -= 1
            
            for _ in range(size):
                node = dq.popleft()
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
                    
            level += 1
        return root
                