class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for rows in board:
            seen = set()
            for j in rows:
                if j == ".": continue
                if j in seen: return False
                else: seen.add(j)

        for y in range(9):
            seen = set()
            for x in range(9):
                if board[x][y] == ".": continue
                if board[x][y] in seen: return False
                else: seen.add(board[x][y])

        for a in range(0,9,3):
            for b in range(0,9,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        if board[a+i][b+j] == ".": continue
                        if board[a+i][b+j] in seen: return False
                        else: seen.add(board[a+i][b+j])

        return True
        


            

        