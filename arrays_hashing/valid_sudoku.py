def isValidSudoku(board):
    grid_map = {}
    for i in range(len(board)//3):
        for j in range(len(board)//3):
            grid_map[(i,j)] = []

    col_arr = [[] for i in range(len(board))]
    for i in range(len(board)):
        row_arr = []
        for j in range(len(board)):
            # print("now",board[i][j])
            if board[i][j] == ".":
                continue
            elif (board[i][j] in row_arr or
                board[i][j] in col_arr[j] or
                board[i][j] in grid_map[(i//3,j//3)]):
                return False
            else:
                row_arr.append(board[i][j])
                col_arr[j].append(board[i][j])
                l = grid_map.get((i//3,j//3))
                l.append(board[i][j])
                grid_map[(i//3,j//3)] = l
    return True

def validSudokuSet(board):
    grid_map ={}
    for i in range(len(board)//3):
        for j in range(len(board)//3):
            grid_map[(i,j)] = set()
    col_arr = [set() for i in range(len(board))]
    for i in range(len(board)):
        row_arr =set()
        for j in range(len(board)):
            if board[i][j] == ".":
                continue
            elif (board[i][j] in row_arr or 
                    board[i][j] in col_arr[j] or
                    board[i][j] in grid_map[(i//3,j//3)]):
                return False
            else:
                row_arr.add(board[i][j])
                col_arr[j].add(board[i][j])
                l = grid_map[(i//3,j//3)]
                l.add(board[i][j])
    return True

    


if __name__ == "__main__":
    board_wrong = [["8","3",".",".","7",".",".",".","."]\
                ,["6",".",".","1","9","5",".",".","."]\
                ,[".","9","8",".",".",".",".","6","."]\
                ,["8",".",".",".","6",".",".",".","3"]\
                ,["4",".",".","8",".","3",".",".","1"]\
                ,["7",".",".",".","2",".",".",".","6"]\
                ,[".","6",".",".",".",".","2","8","."]\
                ,[".",".",".","4","1","9",".",".","5"]\
                ,[".",".",".",".","8",".",".","7","9"]]

    board_right = [["5","3",".",".","7",".",".",".","."]\
                ,["6",".",".","1","9","5",".",".","."]\
                ,[".","9","8",".",".",".",".","6","."]\
                ,["8",".",".",".","6",".",".",".","3"]\
                ,["4",".",".","8",".","3",".",".","1"]\
                ,["7",".",".",".","2",".",".",".","6"]\
                ,[".","6",".",".",".",".","2","8","."]\
                ,[".",".",".","4","1","9",".",".","5"]\
                ,[".",".",".",".","8",".",".","7","9"]]
    
    print(validSudokuSet(board_wrong)) 
