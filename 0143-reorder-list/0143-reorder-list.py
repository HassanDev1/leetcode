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
        
        curr = head
        arr = []
        while curr:
            arr.append(curr)
            curr = curr.next
        
        size  = len(arr)
        l,r = 0,size-1

        count = 0
        while l < r:
            arr[l].next = arr[r]
            l += 1
            arr[r].next = arr[l]
            r -= 1
        arr[l].next = None
       
       
        
        
       
       
        