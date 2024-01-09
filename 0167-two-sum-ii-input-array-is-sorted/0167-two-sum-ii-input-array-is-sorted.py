class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l,r =0, len(numbers)-1
        res = []
        
        while l <= r:
            curr_sum = numbers[l] + numbers[r]
            if target == curr_sum:
                return [l+1,r+1]
            elif target > curr_sum:
                l += 1
            else:
                r -= 1
                
        
            
            
        