# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
      
        
        fast = head
        new_list = slow = ListNode(0,head)
        while n:
            fast = fast.next
            n -= 1
            
        while fast:
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        return new_list.next
        