# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        new_list = prev_node = ListNode(0,head)
        
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                prev_node.next = curr.next
            else:
                prev_node = curr
            curr = curr.next
            
        return new_list.next