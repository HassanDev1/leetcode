class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        row_len = len(matrix)
        col_len = len(matrix[0])
        
        for row in matrix:
            l,r = 0,len(row)-1
            
            while l <= r:
                mid = l + (r-l)//2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    l = mid+1
                else:
                    r = mid-1
                    
            
        return False
                        
        
        