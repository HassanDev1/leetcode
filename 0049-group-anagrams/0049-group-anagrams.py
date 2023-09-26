class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hmap = defaultdict(list)

        for c in strs:
            sorted_string = "".join(sorted(c))
            hmap[sorted_string].append(c)

      
        return hmap.values()
        