class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        check = Counter(s1)
        permutation = {}
        
        l = 0
        for r in range(len(s2)):
            if s2[r] in check:
                permutation[s2[r]] = permutation.get(s2[r],0)+1
                
            if r-l + 1 == len(s1):
                if check == permutation:
                    return True
                if s2[l] in permutation:
                    if permutation[s2[l]] <= 1:
                        del permutation[s2[l]]
                    else:
                        permutation[s2[l]] -= 1
                l += 1
        return False