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
        
        node = []
        curr = head
        
        while curr:
            node.append(curr)
            curr = curr.next
            
        l,r = 0, len(node)-1
        
        while l < r:
            node[l].next = node[r]
            l += 1
            node[r].next = node[l]
            r -= 1
        node[l].next = None