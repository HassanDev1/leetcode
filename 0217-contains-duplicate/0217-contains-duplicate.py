class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        seen = Counter(nums)
        
        for k,v in seen.items():
            if v > 1:
                return True
        return False
        