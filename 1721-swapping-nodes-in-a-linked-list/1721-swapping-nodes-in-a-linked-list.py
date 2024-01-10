# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
        curr = head
        nodes = []
        while curr:
            nodes.append(curr.val)
            curr = curr.next
            
        l = k-1
        r = len(nodes)-k
        
        nodes[l],nodes[r] = nodes[r],nodes[l]
        
        new_list = curr = ListNode()
        
        for node in nodes:
            curr.next = ListNode(node)
            curr = curr.next
        head = new_list.next
        return head
        