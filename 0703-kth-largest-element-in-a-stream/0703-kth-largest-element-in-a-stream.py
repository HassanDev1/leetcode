class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        
        self.heap = []
        self.k = k
        for num in nums:
            heappush(self.heap,num)
            while len(self.heap) > k:
                heappop(self.heap)
        

    def add(self, val: int) -> int:
        heap = self.heap
        k = self.k
        
        heappush(heap,val)
        
        if len(heap) > k:
            heappop(heap)
        return heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)