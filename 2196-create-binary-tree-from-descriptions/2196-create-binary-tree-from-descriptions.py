# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        
        freq = {}
    
        child_set = set()
        
        for p,c,l in descriptions:
            child_set.add(c)
            if p not in freq:
                freq[p] = TreeNode(p)
            if c not in freq:
                freq[c] = TreeNode(c)
            if l:
                freq[p].left = freq[c]
            else:
                freq[p].right = freq[c]
       
        for i in freq.keys():
            if i not in child_set:
                return freq[i]
        
                
       