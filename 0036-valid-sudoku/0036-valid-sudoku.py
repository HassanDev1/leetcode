class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                ele = board[r][c]
                
                if ele.isdigit():
                    res += [(ele,r),(c,ele),(r//3,c//3,ele)]
                    
        return len(res) == len(set(res))
        