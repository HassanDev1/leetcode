class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row_len = len(mat)
        col_len = len(mat[0])
        
        if (r*c) != row_len*col_len:
            return mat
        
        flat = []
        
        for row in mat:
       
            for item in row:
                flat.append(item)
                
        res = []
        k = 0
        for i in range(r):
            temp = []
            for j in range(c):
                temp.append(flat[k])
                k += 1
            res.append(temp)
        return res