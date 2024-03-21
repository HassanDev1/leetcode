class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        res = [0]*26
        freq = defaultdict(list)
        alp_freq = {}
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for i in range(len(alpha)):
            alp_freq[alpha[i]] = i
        
        
        for i in range(len(s)):
            freq[s[i]].append(i)
            
        for char,value in freq.items():
            res[alp_freq[char]] = value[1]-value[0]-1
        print(res)  
        for char in set(s):
            if res[alp_freq[char]] != distance[alp_freq[char]]:
                return False
        
        return True
            