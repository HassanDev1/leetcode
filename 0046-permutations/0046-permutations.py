class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
       
        visited = set()
        
        def dfs(comb):
            if len(comb) == len(nums):
                res.append(comb.copy())
                return
            for i in range(len(nums)):
                if nums[i] in visited:
                    continue
                    
                visited.add(nums[i])
                dfs(comb+[nums[i]])
                visited.remove(nums[i])
                
        dfs([])
        return res
        