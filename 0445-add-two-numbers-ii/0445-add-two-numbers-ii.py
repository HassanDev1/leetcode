# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rev_ll(self,node):
        p1 = None
        while node:
            nxt_node = node.next
            node.next = p1
            p1 = node
            node = nxt_node
        return p1
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        p1 = self.rev_ll(l1)
        p2 = self.rev_ll(l2)
        
        carry = 0
        new_list = curr = ListNode(0)
        
        while p1 or p2 or carry:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            
            total = val1 + val2 + carry
            
            carry = total//10
            curr.next = ListNode(total%10)
            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next
            curr = curr.next
            
        return self.rev_ll(new_list.next)
        
        
        
       
        
        