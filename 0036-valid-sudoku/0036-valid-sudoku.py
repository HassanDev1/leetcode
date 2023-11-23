class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        res = []
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                ele = board[r][c]
                if ele.isalnum():
                    res += [(r,ele),(ele,c),(r//3,c//3,ele)]
                    
                    
        return len(res) == len(set(res))
        