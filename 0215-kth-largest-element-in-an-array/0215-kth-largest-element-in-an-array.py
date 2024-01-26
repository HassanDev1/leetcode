class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []

        for n in nums:
            heappush(heap,n)

        while len(heap) > k:
            heappop(heap)

        return heap[0]