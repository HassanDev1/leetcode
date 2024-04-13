class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        source = image[sr][sc]
        def dfs(i,j):
            if (i < 0 or i > len(image)-1) or (j < 0 or j > len(image[0])-1) or (image[i][j] != source) or image[i][j] == color:
                return
            image[i][j] = color
           
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)
            
        
        
        dfs(sr,sc)         
        return image