class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        for rows in matrix:
            l,r = 0,len(rows)-1
            while l <= r:
                mid = l + (r-l)//2
                if rows[mid] == target:
                    return True
                elif target > rows[mid]:
                    l  = mid + 1
                else:
                    r = mid -1
                    
        return False
        