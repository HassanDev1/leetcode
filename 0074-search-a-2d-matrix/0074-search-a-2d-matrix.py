class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l,r = 0,len(matrix)*len(matrix[0])-1
        row,col = len(matrix),len(matrix[0])
        
        while l <= r:
            mid = l + (r-l)//2
            num = matrix[mid//col][mid%col]
            if num == target:
                return True
            elif target > num:
                l = mid +1
            else:
                r = mid-1
        return False
                
        