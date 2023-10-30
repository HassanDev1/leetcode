class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        res = []
        row_len = len(board)
        col_len = len(board[0])
        
        for r in range(row_len):
            for c in range(col_len):
                ele = board[r][c]
                if ele.isdigit():
                    res += [(ele,r),(c,ele),(r//3,c//3,ele)]
                    
        return len(res) == len(set(res))
        