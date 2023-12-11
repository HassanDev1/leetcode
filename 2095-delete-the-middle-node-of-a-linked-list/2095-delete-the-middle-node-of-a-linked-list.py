# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        new_list = ListNode(0,head)
        left = new_list
        right = head
        
        while right and right.next:
            left = left.next
            right = right.next.next
            
        left.next = left.next.next
        return new_list.next
        