class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        # Create an empty heap
        heap = []   
        
        # Count the occurrences of each number in the list
        count = Counter(arr)
        
        # Add tuples to the min heap (value, key)
        # it will be sorted using the value (with least frequent numbers on top of the heap)
        for key, val in count.items():
            heappush(heap, (val, key))
            
        # Variable to track the number of deletions
        deletion = 0
            
        # Iterate over the heap
        for _ in range(len(heap)):
            # Increment deletion with the count of the smallest element in the heap
            deletion += heap[0][0]
            
            # If the total deletions exceed the allowed limit (k), exit the loop
            if deletion > k:
                break
            
            # Remove the smallest element from the heap
            heappop(heap)
                
        return len(heap)