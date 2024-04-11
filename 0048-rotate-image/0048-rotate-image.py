class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        def helper(top_left, bottom_right):
            # Basecase: Single square 
            if bottom_right <= top_left:
                return

            # Rotate the items from upper-row with left-column, left-column with bottom-row, bottom-row with right-column, and right-column with upper-row
            for i in range(top_left, bottom_right):
                tmp = matrix[top_left][i] # Store upper-row
                matrix[top_left][i] = matrix[n-i][top_left] # Set upper-row with value in left-column
                matrix[n-i][top_left] = matrix[n-top_left][n-i] # Set left-column with value in bottom-row
                matrix[n-top_left][n-i] = matrix[n-(n-i)][n-top_left] # Set bottom-row with value in right-column
                matrix[n-(n-i)][n-top_left] = tmp # Set the right-column with upper-row

            # Recursive reduce the layers
            helper(top_left+1, bottom_right-1)
        
        # Run helper function starting at the outermost layer
        n = len(matrix)-1
        helper(0, n)
        