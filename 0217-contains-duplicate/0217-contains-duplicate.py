class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        found = {}
        for num in nums:
            if num in found:
                return True
            found[num] = 1

        return False
        