# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        
        slow,fast = head,head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        l1,l2 = head,slow
        rev = self.reversell(l2)
        max_sum = 0
        while rev and l1:
            max_sum = max(max_sum,rev.val+l1.val)
            l1 = l1.next
            rev = rev.next
        return max_sum
        
    def reversell(self,head):
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        