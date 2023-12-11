# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        new_list = []
        curr = head
        while curr:
            new_list.append(curr)
            curr = curr.next
            
        l,r =0,len(new_list)-1
        
        while l < r:
            new_list[l].next = new_list[r]
            l += 1
            new_list[r].next = new_list[l]
            r -= 1
            
        new_list[l].next = None
        
            
        