class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        
        for item in matrix:
            l,r =0,len(item)
            
            while l < r:
                mid = l +(r-l)//2
                if item[mid] == target:
                    return True
                elif target > item[mid]:
                    l = mid + 1
                else:
                    r = mid
                    
        return False
        