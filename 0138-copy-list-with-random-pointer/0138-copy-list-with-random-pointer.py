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
        
        
        copyOldToNew = {None:None}
        
        curr = head
        while curr:
            copy = Node(curr.val)
            copyOldToNew[curr] = copy
            curr = curr.next
            
        curr = head
        while curr:
            copy = copyOldToNew[curr]
            copy.next = copyOldToNew[curr.next]
            copy.random = copyOldToNew[curr.random]
            curr = curr.next
            
        return copyOldToNew[head]