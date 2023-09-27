class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        def isTasty(arr,dist,basket):
            first = arr[0]
            count = 1

            for i in range(1,len(arr)):

                if arr[i] - first >= dist:
                    count += 1
                    first = arr[i]

                if count >= basket:
                    return True
            return False
        price.sort()
        l = 1
        r = price[-1]-price[0]

        while l <= r:
            mid = (l +r) //2

            if isTasty(price,mid,k):
                l = mid +1
            else:
                r = mid -1
        return r
        