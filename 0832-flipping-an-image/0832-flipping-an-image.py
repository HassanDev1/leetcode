class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        
        
        for row in image:
            l,r = 0, len(row)-1
            while l < r:
                row[l],row[r] = row[r],row[l]
                l += 1
                r -= 1
            for i,item in enumerate(row):
                if item == 1:
                    row[i] = 0
                else:
                    row[i] = 1
        
        
        return image