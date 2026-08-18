class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_nb = {
            "1":0,
            "2":0,
            "3":0,
            "4":0,
            "5":0,
            "6":0,
            "7":0,
            "8":0,
            "9":0
        }
        for line in range(0, 9):
            current = valid_nb.copy() 
            for i in range(0, 9):
                cell = board[line][i]
                if cell == ".":
                    continue 
                if cell in current:
                    if current[cell] == 1:
                        return False
                    current[cell] += 1
                else:
                    return False

        for row in range(0,9):
            current = valid_nb.copy() 
            for j in range(0,9):
                cell = board[j][row]
                if cell == ".":
                    continue 
                if cell in current:
                    if current[cell]==1: 
                        return False
                    current[cell] += 1
                else: 
                    return False

        for i in range(0,3):
            for j in range(0,3):
                current = valid_nb.copy()
                for line_square in range(i*3,i*3+3):
                    for row_square in range(j*3,j*3+3):
                        cell = board[line_square][row_square]
                        if cell == ".":
                            continue 
                        if cell in current:
                            if current[cell]==1: return False
                            current[cell] += 1
                        else: return False

        return True
