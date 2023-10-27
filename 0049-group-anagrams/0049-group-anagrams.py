class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        
        for ele in strs:
            sorted_ele = "".join(sorted(ele))
            res[sorted_ele].append(ele)
            
        return res.values()
        