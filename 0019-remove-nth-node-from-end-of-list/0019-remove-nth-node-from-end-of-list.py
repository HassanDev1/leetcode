# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        new_list = left = ListNode(0,head)
        fast = head
        
        while n:
            fast = fast.next
            n -= 1
            
        while fast:
            left = left.next
            fast = fast.next
            
        left.next = left.next.next
        
        return new_list.next
        
        