# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        curr = head
        
        nodes = []
        while curr:
            nodes.append(curr)
            curr = curr.next
            
        l=0
        r = len(nodes)-1
        while l < r:
            nodes[l].next = nodes[r]
            l += 1
            nodes[r].next = nodes[l]
            r -= 1
            
        nodes[l].next = None