# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        new_list = ListNode(0,head)
        left = new_list
        fast = head
        
        while n > 0:
            fast = fast.next
            n-=1
        while fast:
            fast = fast.next
            left = left.next
            
        left.next = left.next.next
            
        
        return new_list.next
        