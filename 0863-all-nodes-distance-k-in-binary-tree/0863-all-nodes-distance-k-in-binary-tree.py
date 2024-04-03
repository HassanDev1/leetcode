# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        parent_cache = {}
        def populate_parent(node,parent):
            if not node:
                return
            parent_cache[node] = parent
            
            populate_parent(node.left,node)
            populate_parent(node.right,node)
            
        
        def get_nodes(node,count):
            if not node or node in visited or count > k:
                return
            visited.add(node)
            if count == k:
                res.append(node.val)
                return
            get_nodes(node.left,count+1)
            get_nodes(node.right,count + 1)
            get_nodes(parent_cache[node],count+1)
            
        populate_parent(root,None)
        visited = set()
        res = []
        get_nodes(target,0)
        return res
        