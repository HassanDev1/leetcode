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
            nodes.append(curr.val)
            curr = curr.next
            
        nodes[k-1],nodes[-k] = nodes[-k],nodes[k-1]
        
        new_list = curr = ListNode(0,head)
        
        for node in nodes:
            new_node = ListNode(node)
            curr.next = new_node
            curr = curr.next
            
        return new_list.next