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
        #create a dictionary copy = {None:None}
        #a variable starts from head curr = head
        # traverse the list while saving nodes into the dict
        # while curr
        #   copy[curr] = curr
        #   curr = curr.next
        #re-initiliaze curr to head
        #traverse again the ll
        #while curr:
        #   new_copy = copy[curr]
        #   new_copy.next = copy[curr.next]
        #   new_copy.random = copy[curr.random]
        # return copy[head]
        copy = {None:None}
        curr = head
        while curr:
            copy[curr] = Node(curr.val)
            curr = curr.next
       
        curr = head
        
        while curr:
            new_copy = copy[curr]
            new_copy.next = copy[curr.next]
            new_copy.random = copy[curr.random]
            curr = curr.next
        return copy[head]