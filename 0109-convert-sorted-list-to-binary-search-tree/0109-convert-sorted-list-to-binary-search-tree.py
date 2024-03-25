# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        
        nodes = []
        curr = head
        while curr:
            nodes.append(curr.val)
            curr = curr.next
            
        def rec(nodes):
            if not nodes:
                return
            mid = len(nodes) // 2
            root = TreeNode(nodes[mid])
            root.left = rec(nodes[:mid])
            root.right = rec(nodes[mid+1:])
            return root
        return rec(nodes)
        