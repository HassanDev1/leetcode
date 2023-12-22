# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not p and q or not q and p:
            return False
        
        dq = deque([(p,q)])
        
        while dq:
            size = len(dq)
            
            for _ in range(size):
                p_node,q_node = dq.pop()
                
                if p_node and not q_node or q_node and not p_node:
                    return False
                
                if p_node and q_node and p_node.val != q_node.val:
                    return False
                if p_node and q_node:
                    dq.append((p_node.left,q_node.left))
                    dq.append((p_node.right,q_node.right))
                    
        return True
        