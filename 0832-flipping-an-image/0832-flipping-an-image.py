class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        
        
        for row in image:
            l,r = 0, len(row)-1
            while l < r:
                row[l],row[r] = row[r],row[l]
                l += 1
                r -= 1
        
        for r in range(len(image)):
            for c in range(len(image[0])):
                if image[r][c] == 1:
                    image[r][c] = 0
                else:
                    image[r][c] = 1
        return image