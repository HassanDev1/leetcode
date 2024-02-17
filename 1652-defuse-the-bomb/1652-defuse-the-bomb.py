class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = []
        if k == 0:
            res = [0]*len(code)
            return res
        
        sign = 1
        if k < 0:
            sign = -1
            k *= -1
            
        for i in range(len(code)):
            total = 0
            for j in range (1,k+1):
                total += code[(i+j*sign)%len(code)]
            res.append(total)
            
        return res
        