# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        nodes = []
        curr = head
        while curr:
            nodes.append(curr.val)
            curr = curr.next
            
        nodes.pop(-n)
        if not nodes:
            return None
        
        new_list = curr = ListNode(0,head)
        for node in nodes:
            curr.next = ListNode(node)
            curr = curr.next
        
        return new_list.next