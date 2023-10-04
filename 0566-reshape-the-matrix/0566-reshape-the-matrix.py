class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        row_len = len(mat)
        col_len = len(mat[0])
        
        if r*c != row_len*col_len:
            return mat
        
        flat = []
        for row in mat:
            for col in row:
                flat.append(col)
        print(flat)
        
        i = 0
        res = []
        for row in range(r):
            temp = []
            for col in range(c):
                temp.append(flat[i])
                i+=1
            res.append(temp)
        return res
            
            
        
       
        