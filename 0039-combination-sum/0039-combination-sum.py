class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res  = []
        temp = []
        def dfs(i,target):
            if i >= len(candidates):
                if target == 0:
                    res.append(temp.copy())
                return

            if target >= candidates[i]:
                temp.append(candidates[i])
                dfs(i,target-candidates[i])
                temp.pop()

            dfs(i+1,target)

        dfs(0,target)
        return res