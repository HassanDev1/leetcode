class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        
        
        l,r = 0,len(matrix)-1
        while l < r:
            matrix[l],matrix[r] = matrix[r],matrix[l]
            l += 1
            r -= 1
        res = []
        for c in range(len(matrix[0])):
            temp = []
            for r in range(len(matrix)):
                temp.append(matrix[r][c])
            res.append(temp)
            
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                matrix[r][c] = res[r][c]
                
            
        
        print(matrix)
            
            