class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        res = []
        
        for i in range(len(code)):
            
            if k > 0:
                interim_sum = 0
                j = i+1
                m = k
                while m:
                    interim_sum += code[j%len(code)]
                    j += 1
                    m -= 1
                res.append(interim_sum)
            elif k == 0:
                res.append(0)
                
            else:
                m = k
                j = i-1
                iterim_sum = 0
                while m:
                    iterim_sum += code[j%len(code)]
                    m += 1
                    j -= 1
                res.append(iterim_sum)
        return res
                
                    
                
                
        