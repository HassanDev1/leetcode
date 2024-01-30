# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
            
        left = k-1
        right = -k
        nodes[left].val,nodes[right].val = nodes[right].val,nodes[left].val
        return head