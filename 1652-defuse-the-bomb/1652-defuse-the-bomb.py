class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        res = []
        if k == 0:
            res = [0]*len(code)
            return res
        
        
        for i in range(len(code)):
            if k > 0:
                m = k
                j = i+1
                curr_sum = 0
                while m:
                    curr_sum += code[j%len(code)]
                    j += 1
                    m -= 1
                res.append(curr_sum)
            else:
                m = k
                j = i-1
                curr_sum = 0
                
                while m:
                    curr_sum += code[j%len(code)]
                    j -= 1
                    m += 1
                res.append(curr_sum)
        return res
                
        