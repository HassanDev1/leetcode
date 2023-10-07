class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0
        if len(s)==1:
            return 1
        slow,fast = 0, 1
        max_len = 0
        hmap = {}
        hmap[s[slow]] = 1
        
        while fast < len(s):
            if s[fast] not in hmap:
                max_len = max(max_len,fast - slow+1)
                hmap[s[fast]] = 1
                fast += 1
            else:
                del hmap[s[slow]]
                slow +=1
                
        return max_len
            
        