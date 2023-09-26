class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        res = []
        
        row_len = len(board)
        col_len = len(board[0])
        
        for r in range(row_len):
            for c in range(col_len):
                elem = board[r][c]
                if elem.isdigit():
                    res += [(r,elem),(elem,c),(r//3,c//3,elem)]
        print(res)         
        return len(res) == len(list(set(res)))
        