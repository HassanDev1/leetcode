class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        goupMap = defaultdict(list)
        
        for s in strs:
          
            sorted_s = sorted(s) 
           
            
            goupMap["".join(sorted_s)].append(s)
                
        return goupMap.values()
        
        