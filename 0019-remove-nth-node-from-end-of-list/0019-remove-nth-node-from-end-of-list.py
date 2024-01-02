# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
            
        if size == n: return head.next
        curr = head
        for i in range(1,size-n):
            curr = curr.next
            
        curr.next = curr.next.next
        return head
            
        