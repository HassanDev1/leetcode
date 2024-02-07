# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = new_list = ListNode(0,head)
        second = head
        while n:
            second = second.next
            n -= 1
            
        while first and second:
            first = first.next
            second = second.next
            
        first.next = first.next.next
        return new_list.next
            
        