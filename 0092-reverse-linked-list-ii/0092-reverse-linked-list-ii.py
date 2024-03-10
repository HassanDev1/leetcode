# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head:
            return
        
        nodes = []
        
        curr = head
        while curr:
            nodes.append(curr.val)
            curr = curr.next
            
        while left <= right:
            nodes[left-1],nodes[right-1] = nodes[right-1],nodes[left-1]
            left += 1
            right -= 1
            
        new_list = curr = ListNode()
        
        for node in nodes:
            new_node = ListNode(node)
            curr.next = new_node
            curr = curr.next
        return new_list.next
            