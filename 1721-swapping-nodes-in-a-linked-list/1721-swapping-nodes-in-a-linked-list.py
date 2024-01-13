# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        
       
        curr = head
        nodes = []
        while curr:
            nodes.append(curr.val)
            curr = curr.next
          
        l = k-1
        r = len(nodes)-k
        l = nodes[k-1]
        r = nodes[len(nodes)-k]
        l,r = r,l
        nodes[k-1] = l
        nodes[len(nodes)-k] = r
        
        new_list = curr = ListNode()
        for i in nodes:
            curr.next = ListNode(i)
            curr = curr.next
        return new_list.next
          
        
        

            