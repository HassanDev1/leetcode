class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for row in matrix:
            l,r=0,len(row)-1
            
            while l < r:
                mid = l + (r-l)//2
                if row[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            if row[l] == target:
                return True
        return False
        