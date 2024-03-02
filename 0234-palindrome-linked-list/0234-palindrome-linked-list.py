# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow,fast = head,head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        l1,l2 = head,slow
        rev = self.reverselist(l2)
        
        while l1 and rev:
            if l1.val != rev.val:
                return False
            l1 = l1.next
            rev = rev.next
 
        
        return True
    def reverselist(self,head):
        curr = head
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev
        