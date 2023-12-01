class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        for ele in matrix:
            l,r= 0,len(ele)-1
            
            while l <= r:
                mid = l + (r-l)//2
                
                if ele[mid] == target:
                    return True
                elif target > ele[mid]:
                    l = mid + 1
                else:
                    r = mid-1
        return False
        