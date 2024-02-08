# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        q = deque([(root,0)])
        max_width = 0
        
        while q:
            size = len(q)
            max_width = max(max_width,q[-1][1] - q[0][1]+1)
            
            for _ in range(size):
                node,index = q.popleft()
                
                if node.left:
                    q.append((node.left,index*2))
                if node.right:
                    q.append((node.right,2*index+1))
                    
        return max_width
        