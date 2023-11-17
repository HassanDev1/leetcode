class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hmap = {}
        
        for c in strs:
            sorted_str = "".join(sorted(c))
            if sorted_str not in hmap:
                hmap[sorted_str] = [c]
            else:
                hmap[sorted_str].append(c)
                
        return hmap.values()
        