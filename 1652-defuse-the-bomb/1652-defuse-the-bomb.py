class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        if k == 0:
            res = [0]*len(code)
            return res
        res = [0]*len(code)
        for i in range(len(code)):
            if k > 0:
                m = k
                j = i+1
                curr_sum = 0
                while m:
                    curr_sum += code[j%len(code)]
                    res[i] = curr_sum
                    m-=1
                    j += 1
            else:
                m = k
                j = i-1
                curr_sum = 0
                while m:
                    curr_sum += code[j%len(code)]
                    res[i] = curr_sum
                    m += 1
                    j -= 1
        return res