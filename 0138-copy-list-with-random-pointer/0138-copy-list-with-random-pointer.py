"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        curr = head
        copyToNode = {None:None}
        
        while curr:
          
            copyToNode[curr] = Node(curr.val)
            curr = curr.next
            
        curr = head
        
        while curr:
            copy = copyToNode[curr]
            copy.next = copyToNode[curr.next]
            copy.random = copyToNode[curr.random]
            curr = curr.next
            
        return copyToNode[head]