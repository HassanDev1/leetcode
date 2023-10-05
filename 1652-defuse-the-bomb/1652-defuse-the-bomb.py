class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        
        res = []
        
        for c in range(len(code)):
            
            if k > 0:
                curr_sum = 0
                m = k
                j = c + 1
                while m:
                    curr_sum += code[j%len(code)]
                    j += 1
                    m -= 1
                res.append(curr_sum)
            elif k == 0:
                res.append(0)
            else:
                curr_sum = 0
                m = k
                j = c - 1
                while m:
                    curr_sum += code[j%len(code)]
                    j -= 1
                    m += 1
                res.append(curr_sum)
        return res
        