class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "X":
                    if (r==0 or board[r-1][c]==".") and (c ==  0 or board[r][c-1] == "."):
                        count += 1
                        
        return count
        