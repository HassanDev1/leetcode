class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def aux(amount):

            if amount == 0:
                return 0

            if amount < 0:
                return float('inf')

            if amount in cache:
                return cache[amount]

            cache[amount] = min([1+aux(amount-c) for c in coins])
            return cache[amount]

        ans = aux(amount)
        if ans == float('inf'):
            return -1
        return ans