class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        row_len = len(board)
        col_len = len(board[0])
        
        seen = set()
        res = []
        
        for r in range(row_len):
            for c in range(col_len):
                num = board[r][c]
                if num.isalnum():
                    res += [(num,r),(c,num),(r//3,c//3,num)]
                    
                    
        return len(res) == len(set(res))