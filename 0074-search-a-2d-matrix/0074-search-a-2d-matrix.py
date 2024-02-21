class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        for row in matrix:
            l,r =0,len(row)-1
            while l <= r:
                mid = l + (r-l)//2
                if row[mid] == target:
                    return True
                elif target > row[mid]:
                    l = mid + 1
                else:
                    r = mid-1
                    
        return False