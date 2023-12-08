class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = {}
        
        for s in strs:
            sort_s = "".join(sorted(s))
            if sort_s not in anagram:
                anagram[sort_s] = [s]
            else:
                anagram[sort_s].append(s)
                
        return anagram.values()
        